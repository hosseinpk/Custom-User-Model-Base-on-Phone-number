from django.db import models
from accounts.usermanager import UserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import(
    AbstractBaseUser,
    PermissionsMixin
)
# Create your models here.






class User(AbstractBaseUser, PermissionsMixin):

    phone = models.CharField(unique=True,max_length=13)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):

        return self.phone
    