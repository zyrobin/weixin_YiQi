# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-09 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0025_auto_20180709_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityimagesmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ActivityImagesModel/%y/%d/51e53f38afc449c09f0214a95e8813ae', verbose_name='活动图片'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='Activity/%y/%d/51e53f38afc449c09f0214a95e8813ae', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='groupcode',
            field=models.ImageField(blank=True, null=True, upload_to='Activity/qr/%y/%d/51e53f38afc449c09f0214a95e8813ae', verbose_name='群二维码'),
        ),
        migrations.AlterField(
            model_name='activitytypemodel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='ActivityTypeModel/%y/%d/51e53f38afc449c09f0214a95e8813ae', verbose_name='类别图片'),
        ),
        migrations.AlterField(
            model_name='slidemodels',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='SlideModels/%y/%d/51e53f38afc449c09f0214a95e8813ae', verbose_name='幻灯片图片'),
        ),
    ]
