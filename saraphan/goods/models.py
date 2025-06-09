from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.db import models

from saraphan.constants import MAX_LENGTH, MAX_TEXT_LENGHT


class Category(models.Model):
    name = models.CharField('Категория', max_length=MAX_LENGTH)
    slug = models.SlugField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField('Подкатегория', max_length=MAX_LENGTH)
    slug = models.SlugField()
    image = models.ImageField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories',
    )

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Название рецепта'
    )
    slug = models.SlugField()
    image = models.ImageField()
    text = models.TextField(
        verbose_name='Описание',
        max_length=MAX_TEXT_LENGHT
    )
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField('Цена', )
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 100)],
                                     format='JPEG',
                                     options={'quality': 80})
    image_medium = ImageSpecField(source='image',
                                  processors=[ResizeToFill(500, 500)],
                                  format='JPEG',
                                  options={'quality': 90})
    image_large = ImageSpecField(source='image',
                                 processors=[ResizeToFill(1000, 1000)],
                                 format='JPEG',
                                 options={'quality': 95})

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class CartGoods(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    amount = models.IntegerField()
