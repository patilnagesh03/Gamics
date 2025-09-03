from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserRegister(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique  

    def __str__(self):
        return self.username  # Return the username for easy identification