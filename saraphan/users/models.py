from django.contrib.auth.models import AbstractUser
from django.db import models

from goods.models import Goods, CartGoods


class User(AbstractUser):
    avatar = models.ImageField()
    cart = models.ManyToManyField(Goods, through=CartGoods)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
