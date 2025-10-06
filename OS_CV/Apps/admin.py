from django.contrib import admin
from .models import webApp

@admin.register(webApp)
class AppAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)