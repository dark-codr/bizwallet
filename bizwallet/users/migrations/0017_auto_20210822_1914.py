# Generated by Django 3.1.12 on 2021-08-22 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210822_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_testified',
            field=models.BooleanField(default=False, verbose_name='User has testified'),
        ),
        migrations.AlterField(
            model_name='payhistory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_pay_history', to=settings.AUTH_USER_MODEL),
        ),
    ]
