# Generated by Django 2.0.3 on 2018-03-14 07:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180314_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pic',
            field=models.ImageField(blank=True, upload_to='post_pic'),
        ),
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 14, 7, 52, 56, 165499, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='quote',
            field=models.TextField(blank=True, null=True),
        ),
    ]
