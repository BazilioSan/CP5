from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(
        max_length=50,
        verbose_name="First name",
        blank=True,
        null=True,
        help_text="Enter username",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Last name",
        blank=True,
        null=True,
        help_text="Enter surname",
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Phone number",
        blank=True,
        null=True,
        help_text="Enter phone number",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Avatar",
        blank=True,
        null=True,
        help_text="Upload avatar",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="City",
        blank=True,
        null=True,
        help_text="Enter city",
    )
    username_tg = models.CharField(
        max_length=255, verbose_name="username tg", null=True, blank=True
    )
    chat_id = models.CharField(
        max_length=255, verbose_name="chat_id", null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
