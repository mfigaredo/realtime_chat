# Generated by Django 5.0.4 on 2024-04-21 02:02

import shortuuid.main
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0002_chatgroup_users_online'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgroup',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='chat_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True),
        ),
    ]
