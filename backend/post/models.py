from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    name = models.CharField('Название', max_length=50, blank=True, null=True)
    description = models.TextField('Описание')
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True
        )
    image = models.ImageField('Изображение', upload_to='post/%Y/%m/%d/', default='', blank=True, null=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2, blank=True, null=True)
    orders = models.DecimalField('Заказы', max_digits=5, decimal_places=2, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'    


    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField('Текст')
    created = models.DateTimeField(auto_now_add=True)




