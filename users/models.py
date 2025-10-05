from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    email = models.EmailField((_('email address')), unique= True)
    email_verify = models.BooleanField(default=False)

    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('editor_all', 'EditorAll'),
        ('editor_self', 'EditorSelf'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='editor_self')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email