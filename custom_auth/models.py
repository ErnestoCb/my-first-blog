from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class CustomUserManager(UserManager):
    def create_superuser(self, run, email, pichula):
        User = CustomUser()
        User.set_password(pichula)
        User.run = run
        User.email = email
        User.save()
        return user

class CustomUser(AbstractUser):
    USERNAME_FIELD = ('run')
    REQUIRED_FIELDS = ('pichula', 'email')
    email = models.EmailField(unique=True)
    run = models.CharField(max_length=10, unique=True)
    pichula = models.CharField(max_length=100, unique=True)
    objects = CustomUserManager()
    class Meta:
        ordering = ['run']