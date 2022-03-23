from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    favdrink = models.CharField(max_length=256, blank=True, null=True)
    pass
    
    
    def __str__(self):
        return self.username