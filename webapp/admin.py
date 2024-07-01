from django.contrib import admin

# Register your models here.
from webapp.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price', 'date_added']
    list_filter = ['category', 'date_added', 'price']
    list_display_links = ['id', 'title', 'category', 'price', 'date_added']
    search_fields = ['title', 'description']
    readonly_fields = ['date_added']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['id', 'title', 'description']
    search_fields = ['title', 'description']


# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
