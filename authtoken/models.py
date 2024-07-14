from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from .extensions import generate_token

class APIKey(models.Model):
    token = models.CharField(max_length=120)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="key")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "token"
        verbose_name_plural = "tokens"

    def save(self, *args, **kwargs):
        # genrate random hashed token 
        if not self.token:
            self.token = generate_token()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.user.username}"