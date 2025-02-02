# Generated by Django 5.1.5 on 2025-02-01 17:03

import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        help_text="Enter username",
                        max_length=50,
                        null=True,
                        verbose_name="First name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        help_text="Enter surname",
                        max_length=50,
                        null=True,
                        verbose_name="Last name",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        help_text="Enter phone number",
                        max_length=15,
                        null=True,
                        verbose_name="Phone number",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        help_text="Upload avatar",
                        null=True,
                        upload_to="users/avatars",
                        verbose_name="Avatar",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        help_text="Enter city",
                        max_length=50,
                        null=True,
                        verbose_name="City",
                    ),
                ),
                (
                    "username_tg",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="username_tg",
                    ),
                ),
                (
                    "chat_id",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="chat_id"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
