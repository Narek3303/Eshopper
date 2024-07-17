from django.contrib import admin
from .models import Category, Product, Profile
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name', 'slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created', 'updated', 'available']
    list_filter = ['name', 'category', 'price', 'created', 'updated', 'available']
    search_fields = ['name', 'category', 'price', 'created']
    list_editable = ['price', 'available']

admin.site.register(Carousel_Header)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(ModelColor)
admin.site.register(ModelSize)
admin.site.register(Image)
