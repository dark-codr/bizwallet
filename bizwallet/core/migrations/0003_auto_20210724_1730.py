# Generated by Django 3.1.12 on 2021-07-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210724_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesvariations',
            name='duration',
            field=models.CharField(blank=True, choices=[('0', '0'), ('28', '28'), ('64', '64'), ('112', '112'), ('168', '168'), ('336', '336'), ('672', '672')], default='168', max_length=4, null=True, verbose_name='Duration'),
        ),
    ]
