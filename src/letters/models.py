from django.db import models


class Letter(models.Model):
    title = models.CharField(max_length=50, verbose_name="Наименование сообщения")
    text = models.TextField(max_length=512, verbose_name="Текст")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
