from django.contrib import admin

from accounts.models import Account
from django.contrib.admin import ModelAdmin


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_display = ("email", "username", "date_joined", "is_admin", "is_active", "is_staff", "is_superuser",)
    search_fields = ("email", "username",)
