from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class MailingModelAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "patronymic", "phone")
