from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'image')
    search_fields = ('brand', 'model')
    list_filter = ('year',)

