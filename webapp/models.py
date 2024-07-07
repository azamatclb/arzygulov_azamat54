from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name="Наименование")
    description = models.TextField(max_length=150, blank=True, default='Нет Описания', verbose_name='Описание')

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    title = models.CharField(max_length=30, verbose_name="Наименование")
    description = models.TextField(max_length=150, null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    date_added = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    image = models.URLField(max_length=5000, unique=True, verbose_name='Изображение')
    in_stock = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return f"{self.id} {self.title} ({self.category}) - {self.price}"

    class Meta:
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
