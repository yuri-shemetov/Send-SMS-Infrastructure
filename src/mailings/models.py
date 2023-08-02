from django.db import models

import uuid

from clients.models import Client
from letters.models import Letter


class Mailing(models.Model):
    MAILING_STATUSES = [
        ("CREATED", "Создано"),
        ("SENT", "Отправлено"),
        ("RECEIVED", "Получено"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    active = models.Manager()

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
