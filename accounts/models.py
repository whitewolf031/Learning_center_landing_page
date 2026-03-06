from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager

class CustomUser(AbstractUser):
    # Username ni butunlay o‘chiramiz yoki ixtiyoriy qoldiramiz
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        null=True,
        db_index=True,
    )

    phone_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Telefon raqami",
    )
    phone_verified = models.BooleanField(default=False, verbose_name="Tasdiqlangan")

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number or "No phone"

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"