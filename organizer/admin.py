from django.contrib import admin

from django.contrib.admin import ModelAdmin
from .models import Tag, Enterprise, NewsLink
from django.utils.translation import gettext_lazy as _


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    search_fields = ("name", "slug",)
    list_display = ("name", "slug",)


@admin.register(Enterprise)
class EnterpriseAdmin(ModelAdmin):
    search_fields = ("name", "slug", "tags__slug", "tags__name",)
    list_display = ("name", "slug", "description", "founded_date", "contact", "website",)
    list_filter = ("tags",)
    fieldsets = (
        (None, {"fields": ("name", "slug", "description",)}),
        (_("Data"), {"fields": ("founded_date", "contact", "website", "tags",)}),
    )


@admin.register(NewsLink)
class NewsLinkAdmin(ModelAdmin):
    search_fields = ("name", "slug", "enterprise__slug", "enterprise__name",)
    list_display = ("name", "slug", "pub_date", "link", "enterprise",)
    fieldsets = (
        (None, {"fields": ("name", "slug", "pub_date", "link", "enterprise",)}),
    )
