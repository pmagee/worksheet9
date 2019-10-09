from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','stock', 'price']
    list_filter = ['price']
    list_editable = ['price', 'stock']


