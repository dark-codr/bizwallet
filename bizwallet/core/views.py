from __future__ import absolute_import

import json
import os

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import BadHeaderError, EmailMessage, send_mail, send_mass_mail
from django.http import Http404, HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from tinymce.views import render_to_image_list

from bizwallet.users.forms import TestimonyForm
from bizwallet.users.models import Testimonial

from .forms import ContactForm, EmailSubscribeForm
from .models import EmailSubscribe, Services

User = get_user_model()

devnull = open(os.devnull, "w")


def compress_whitespace(s):
    return " ".join(s.split())

def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', None)    ### Real IP address of client Machine
    return ip  

@cache_page(60 * 10)  # cached in 1 second.. for 15 minutes (60 sec x 15mins)
@csrf_protect
def home(request, *args, **kwargs):
    # get referrer linked to reffered using username
    username = str(kwargs.get("username"))

    ip_address = get_ip_address(request)
    print(ip_address)

   
    services = Services.objects.all().filter(active=True)
    testimonials = Testimonial.objects.filter(active=True).order_by("-created")[:5]

    try:
        user = User.objects.get(username=username)
        if user.is_field_worker:
            request.session["fieldworker_id"] = user.id
            user_ip = request.session["fieldworker_id"]
    except:
        pass



    try:
        is_cached = "geodata" in request.session
        # get user ip and get information of the user
        if not is_cached:
            response = requests.get(f"https://reallyfreegeoip.org/json/{ip_address}")
            request.session["geodata"] = response.json()

        geodata = request.session["geodata"]
        print(geodata)
        request.session["user_ip"] = geodata["ip"]
        request.session["country"] = geodata["country_name"]
        print(request.session.get("country"))
        request.session["country_code"] = geodata["country_code"]
        request.session["region_name"] = geodata["region_name"]
        request.session["city"] = geodata["city"]
    except:
        pass

    if not request.session.get("user_ip"):
        messages.info(
            request,
            _(
                "Welcome to Bizwallet Co-Operative. Please feel free to communicate any challanges with the support team."
            ),
        )

    if request.method == 'POST':
        form = TestimonyForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('home'))
            messages.success(request, "Your review has been submitted successfuly")
            send_mail("New Testimonial Submitted", "Some Just submitted a new testimonial", "no-reply@bizwallet.org", ['info@bizwallet.org'], fail_silently=False)
    else:
        form = TestimonyForm()

    return render(request, "pages/home.html", {"form":form, "is_cached": is_cached, "services": services, "testimonials": testimonials})


class ServiceListView(DetailView):
    model = Services
    template_name = 'pages/services.html'
    context_object_name = 'services'
    queryset = Services.objects.filter(active=True)

    def get_object(self, queryset=None):
        return Services.objects.get(pk=self.kwargs.get("pk"))

service_detail = ServiceListView.as_view()


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            html_message = render_to_string('email/support_mail.html', {'message': message, 'from_email': from_email, 'subject': subject})

            try:
                send_mail(subject, message, from_email, ['info@bizwallet.org'], html_message=html_message, fail_silently=False)
                messages.success(request, "Your Email Has been sent successfuly")
            except BadHeaderError:
                messages.error(request, "There was an error sending yout email at the moment, please try again later.")
                # return HttpResponse('Invalid Header found')
            return redirect('home')
    return render(request, 'pages/contact.html', {'form': form})



class UserEmailSubscribe(SuccessMessageMixin, CreateView):

    model = EmailSubscribe
    template_name = "snippets/footer.html"
    form_class = EmailSubscribeForm
    success_url = reverse_lazy("home")
    success_message = _("Email successfully added to our email list")

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())

email_subscribe = UserEmailSubscribe.as_view()
