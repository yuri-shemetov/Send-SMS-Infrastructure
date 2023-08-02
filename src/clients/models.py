from django.db import models
from django.urls import reverse


class Client(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
    )
    patronymic = models.CharField(
        blank=True,
        max_length=50,
        db_index=True,
        verbose_name="Отчество",
    )
    phone = models.CharField(
        unique=True,
        null=False,
        db_index=True,
        max_length=17,
        help_text="+375(29)123-45-67",
        verbose_name="Моб. тел.",
    )
    email = models.EmailField(
        unique=True,
        null=True,
        max_length=100,
        help_text="user@gmail.com",
        verbose_name="Почта",
    )
    created_at = models.DateTimeField(
        verbose_name="Загружено в базу",
        auto_now=False,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Обновлено в базе",
        auto_now=True,
        auto_now_add=False,
    )

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.patronymic} - {self.phone}"

    def get_absolute_url(self):
        return reverse("clients")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
