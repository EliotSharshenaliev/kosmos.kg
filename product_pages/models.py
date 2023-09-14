from django.db import models


class Country(models.Model):
    county = models.CharField(max_length=100, verbose_name="Страны")

    def __str__(self):
        return str(self.county)

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class ColorsProduct(models.Model):
    color = models.CharField(verbose_name='Цветы товара', max_length=50)

    def __str__(self):
        return str(self.color)

    class Meta:
        verbose_name = "Цвет продукта"
        verbose_name_plural = "Цветы продуктов"


class SizesProduct(models.Model):
    size = models.CharField(verbose_name='Размеры товара', max_length=50)

    def __str__(self):
        return str(self.size)

    class Meta:
        verbose_name = "Размер продукта"
        verbose_name_plural = "Размеры продуктов"


class PhotoProduct(models.Model):
    photo = models.ImageField(
        upload_to='images/products/',
        verbose_name="Картинки"
    )

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Фото продукта"
        verbose_name_plural = "Фотографии продуктов"


class Orderer(models.Model):
    firstname = models.CharField(max_length=50, verbose_name="Имя")
    lastname = models.CharField(max_length=50, verbose_name="Фамилия")
    number_phone = models.IntegerField(verbose_name="Номер телефона")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Страна", null=True)
    city = models.CharField(max_length=50, verbose_name="Город")
    store_location = models.CharField(max_length=50, verbose_name="Адресс/ТЦ")
    store = models.CharField(max_length=50, verbose_name="Магазин", null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Categorie(models.Model):
    type = models.CharField(verbose_name="Тип категории (en)", max_length=50)
    title = models.CharField(verbose_name="Название категории", max_length=100)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategorie(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='category', null=True)
    type = models.CharField(verbose_name="Тип под категории (en)", max_length=50)
    title = models.CharField(verbose_name="Название под категории", max_length=100)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Product(models.Model):
    category = models.ForeignKey(
        Categorie,
        verbose_name="Категория товара",
        on_delete=models.CASCADE)

    subcategory = models.ForeignKey(
        Subcategorie,
        null=True,
        verbose_name="Под категория товара",
        on_delete=models.CASCADE
    )

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

    description = models.CharField(
        verbose_name="Описание товара",
        max_length=255,
        null=True
    )

    orderer = models.ManyToManyField(
        Orderer,
        related_name='products',
        verbose_name="Заказ",
        editable=False
    )

    photos = models.ManyToManyField(
        PhotoProduct,
        related_name='photos',
        verbose_name="Фото"
    )

    color = models.ManyToManyField(
        ColorsProduct,
        verbose_name="Цвет товара",
        editable=False
    )

    size = models.ManyToManyField(
        SizesProduct,
        related_name='sized',
        verbose_name="Размеры товара",
        editable=False
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class OrderItem(models.Model):
    order = models.ForeignKey(Orderer, on_delete=models.CASCADE, verbose_name="Заказчик")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    count = models.PositiveIntegerField(verbose_name="Количество")
    created = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def total_amount(self):
        return self.product.price * self.count

    def __str__(self):
        return f"{self.product} x{self.count}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
