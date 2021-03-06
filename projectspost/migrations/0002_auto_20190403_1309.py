# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 13:09
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectspost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to=b'projects/')),
                ('description', models.TextField(max_length=500)),
                ('link', models.TextField(null=True, validators=[django.core.validators.URLValidator()])),
                ('design', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1)),
                ('usability', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1)),
                ('content', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commenter',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_photo',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
