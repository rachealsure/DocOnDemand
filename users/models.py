from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username


