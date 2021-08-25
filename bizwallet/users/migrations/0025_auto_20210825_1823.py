# Generated by Django 3.1.12 on 2021-08-25 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20210825_1719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'managed': True, 'ordering': ['-created', '-modified'], 'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.RenameField(
            model_name='banks',
            old_name='code',
            new_name='bank_code',
        ),
    ]
