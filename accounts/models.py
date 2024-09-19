from django.db import models
from accounts.manager import UserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import(
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.validators import RegexValidator  



phone_number_validator = RegexValidator(  
    regex=r'^(\+98|0)?9\d{9}$',  # Example regex for phone numbers  
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."  
)  

class User(AbstractBaseUser, PermissionsMixin):

    phone = models.CharField(unique=True,max_length=13, validators=[phone_number_validator])
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
    