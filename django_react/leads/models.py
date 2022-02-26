from django.db import models
import datetime


class Lead(models.Model):
    name = models.CharField(max_length=100, default="name")
    email = models.EmailField(default="email")
    message = models.CharField(max_length=300, default="massage")
    created_at = models.DateTimeField(auto_now_add=True)
