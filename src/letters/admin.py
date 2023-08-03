from django.contrib import admin

from letters.models import Letter


@admin.register(Letter)
class MailingModelAdmin(admin.ModelAdmin):
    list_display = ("title", "text")
