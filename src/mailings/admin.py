from django.contrib import admin

from mailings.models import Mailing


@admin.register(Mailing)
class MailingModelAdmin(admin.ModelAdmin):
    list_display = ("mailing_text", "send_date", "status")
