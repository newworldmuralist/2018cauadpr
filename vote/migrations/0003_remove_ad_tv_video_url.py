# Generated by Django 2.0.7 on 2018-07-29 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20180713_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad_tv',
            name='video_url',
        ),
    ]
