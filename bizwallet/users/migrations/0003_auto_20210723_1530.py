# Generated by Django 3.1.12 on 2021-07-23 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210723_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'FieldWorker',
                'verbose_name_plural': 'FieldWorkers',
                'ordering': ['-created', '-modified'],
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='investor',
            name='user',
        ),
        migrations.DeleteModel(
            name='FieldWorker',
        ),
        migrations.DeleteModel(
            name='Investor',
        ),
    ]
