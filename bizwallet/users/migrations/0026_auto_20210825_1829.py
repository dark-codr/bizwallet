# Generated by Django 3.1.12 on 2021-08-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20210825_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_number',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='Account Number'),
        ),
    ]
