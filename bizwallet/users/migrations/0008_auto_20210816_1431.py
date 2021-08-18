# Generated by Django 3.1.12 on 2021-08-16 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_testimonial_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='plan',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userplan', to='users.enrollmentplan'),
        ),
    ]