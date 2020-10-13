from django.contrib import admin

from django.contrib.admin import ModelAdmin
from .models import Tag

@admin.register(Tag)
class TagAdmin(ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "slug",)
    list_filter = ("name", "slug",)
