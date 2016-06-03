# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpansionUsers',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(upload_to=b'users_image', verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
                ('biometric_number', models.CharField(max_length=40, verbose_name='\u0411\u0442\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043e\u0434', blank=True)),
                ('skype', models.CharField(max_length=40, verbose_name='Skype', blank=True)),
                ('icq', models.CharField(max_length=40, verbose_name='Icq', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
    ]
