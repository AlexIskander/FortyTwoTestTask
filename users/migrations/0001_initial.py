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
                ('biometric_number', models.CharField(max_length=40, verbose_name='\u0411\u0438\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043e\u0434', blank=True)),
                ('skype', models.CharField(max_length=40, verbose_name='Skype', blank=True)),
                ('icq', models.CharField(max_length=40, verbose_name='jaber', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0436\u0435\u043d\u0438\u044f', blank=True)),
                ('other', models.TextField(verbose_name='\u0414\u0440\u0443\u0433\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435', blank=True)),
            ],
            options={
                'ordering': ['username'],
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438',
            },
            bases=('auth.user',),
        ),
    ]
