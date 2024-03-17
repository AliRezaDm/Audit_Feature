from django.contrib import admin
from .models import Supply, Category

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'status', 'count')
    list_filter = (['id', 'status'])
    search_fields = ('id', 'title')
    ordering = ['id', 'count']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'title')
    list_filter = (['id', 'title'])
    search_fields = ('id', 'title')
    ordering = ['id']
