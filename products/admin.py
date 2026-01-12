from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_trending', 'is_featured', 'is_available')
    list_filter = ('category', 'is_trending', 'is_featured', 'is_available')
    prepopulated_fields = {'slug': ('name',)}
