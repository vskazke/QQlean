from django.db import models


class CallBack(models.Model):
        phone = models.CharField(max_length=200)
        summ_room = models.CharField(max_length=200, default='', null=True)
        summ_bath = models.CharField(max_length=200, default='', null=True)

class Short(models.Model):
        phone = models.CharField(max_length=200)
