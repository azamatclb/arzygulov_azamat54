from django.db import models


# Create your models here.

class Category(models.Model):
    tittle = models.CharField(max_length=30, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=150, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.id} {self.tittle} {self.description}"

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    tittle = models.CharField(max_length=30, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=150, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    date_added = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    image = models.URLField(max_length=1000, unique=True, null=False, blank=False, verbose_name='Изображение')

    def __str__(self):
        return f"{self.id} {self.tittle} {self.category} {self.price}"

    class Meta:
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
