from django.contrib import admin
from .models import Supply, Category, Variant

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):

    list_display = ('id', 'image_tag','title', 'status')
    list_filter = (['id', 'status'])
    search_fields = ('id', 'title')
    ordering = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'title')
    list_filter = (['id', 'title'])
    search_fields = ('id', 'title')
    ordering = ['id']

@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):

    list_display = ('supply', 'color', 'size', 'count')
  