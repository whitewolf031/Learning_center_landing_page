from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Mazmun")
    image = models.ImageField(
        upload_to='news/images/',
        null=True,
        blank=True,
        verbose_name="Rasm"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name="Muallif"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")

    class Meta:
        ordering = ['-created_at']   
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title