# Generated by Django 3.1.12 on 2021-08-25 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_profile_blacklisted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='verified',
            new_name='is_verified',
        ),
    ]
