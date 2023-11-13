from django.contrib import admin

from .models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ("__str__","slug")
    class Meta:
        model = Products

admin.site.register(Products, ProductAdmin)