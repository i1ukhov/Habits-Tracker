from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="email", help_text="Email address"
    )
    phone = models.CharField(
        max_length=35, verbose_name="phone", help_text="Enter phone number", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Photo",
        help_text="Upload your avatar",
        **NULLABLE,
    )
    city = models.CharField(
        max_length=100, verbose_name="city", help_text="Enter city", **NULLABLE
    )
    tg_chat_id = models.CharField(
        max_length=100, verbose_name="tg_chat_id", help_text="Enter chat ID", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"Пользователь №{self.pk}. Email: {self.email}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
