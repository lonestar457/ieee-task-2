from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    is_customer = models. BooleanField(default=False)
    is_eng = models. BooleanField(default=False)

    def _str_(self):
        return self.username