# -*- coding: utf-8 -*-

from django.db import models


class CallBack(models.Model):
        phone = models.CharField('Телефон', max_length=200)
        summ_room = models.CharField('Кол-во комнат', max_length=200, default='', null=True)
        summ_bath = models.CharField('Кол-во саузлов', max_length=200, default='', null=True)

class Short(models.Model):
        phone = models.CharField('Телефон', max_length=200)
