from django.db import models

from clients.models import Client
from letters.models import Letter


class Mailing(models.Model):
    MAILING_STATUSES = [
        ("CREATED", "Создано"),
        ("SENT", "Отправлено"),
        ("RECEIVED", "Получено"),
    ]

    clients = models.ManyToManyField(Client, verbose_name="Список клиентов")
    mailing_text = models.ForeignKey(
        Letter,
        on_delete=models.CASCADE,
        related_name="mailings",
        verbose_name="Сообщение",
    )
    send_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        default="CREATED",
        choices=MAILING_STATUSES,
        verbose_name="Статус",
    )

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
