from django.db import models


class Task(models.Model):
    # Django добавляет первичный ключ id автоматически.
    title = models.CharField("Название", max_length=120)
    done = models.BooleanField("Выполнена", default=False)
    created_at = models.DateTimeField("Добавлена", auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
