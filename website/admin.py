from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _

from .models import Post


@admin.register(Post)
class PostAdmin(ModelAdmin):
    search_fields = ("title", "slug", "tags__slug", "tags__name", "enterprise__slug", "enterprise__name")
    list_display = ("title", "slug", "pub_date", "enterprise",)
    list_filter = ("tags",)
    fieldsets = (
        (None, {"fields": ("title", "slug", "pub_date", "enterprise",)}),
        (_("Data"), {"fields": ("content", "tags",)}),
    )

