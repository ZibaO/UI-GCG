# Generated by Django 2.0.7 on 2018-07-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180721_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date_requested',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت درخواست'),
        ),
    ]
