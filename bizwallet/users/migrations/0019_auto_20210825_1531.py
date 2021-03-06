# Generated by Django 3.1.12 on 2021-08-25 14:31

import datetime
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20210824_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Bank Name')),
                ('slug', models.SlugField(blank=True, max_length=700, null=True, unique=True)),
                ('code', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Bank Code')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False, verbose_name='User is Verified'),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='ver_expired',
            field=models.DateField(default=datetime.date(2021, 8, 28)),
        ),
    ]
