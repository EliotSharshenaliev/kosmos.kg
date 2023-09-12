from PIL import Image
from django.db import models


class Categories(models.Model):
    type = models.CharField(verbose_name="Тип категории", max_length=50)
    title = models.CharField(verbose_name="Название категории", max_length=100)

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    category = models.OneToOneField(
        Categories,
        verbose_name="Категория товара",
        on_delete=models.CASCADE)
    price = models.DecimalField(
        verbose_name="Цена товара",
        max_digits=6,
        decimal_places=2
    )
    currency = models.CharField(
        verbose_name="Валюта",
        max_length=2)
    title = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Название товара"
    )

    def __str__(self):
        return self.title


class PhotoProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(
        upload_to='static/images/products/',
        verbose_name="Картинки"
    )

    def __str__(self):
        return str(self.photo)
