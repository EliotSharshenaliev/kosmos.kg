from django.db import models


class FeedbackMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя", null=True)
    email = models.CharField(max_length=100, verbose_name="Email")
    msg = models.CharField(max_length=255, verbose_name="Сообщение")
    sent = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=100, verbose_name="Номер телефона", null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"
