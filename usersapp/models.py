from django.db import models

class Player(models.Model):
    nick_name = models.CharField(max_length=55)
