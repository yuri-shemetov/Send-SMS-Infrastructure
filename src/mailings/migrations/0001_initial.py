# Generated by Django 4.2.4 on 2023-08-03 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("clients", "0001_initial"),
        ("letters", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("send_date", models.DateTimeField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CREATED", "Создано"),
                            ("SENT", "Отправлено"),
                            ("RECEIVED", "Получено"),
                        ],
                        default="CREATED",
                        max_length=10,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "clients",
                    models.ManyToManyField(
                        to="clients.client", verbose_name="Список клиентов"
                    ),
                ),
                (
                    "mailing_text",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mailings",
                        to="letters.letter",
                        verbose_name="Сообщение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
    ]
