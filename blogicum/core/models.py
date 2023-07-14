from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
