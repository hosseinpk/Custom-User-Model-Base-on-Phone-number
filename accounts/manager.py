import re
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):

    @staticmethod
    def phone_validate(phone):

        phone = str(phone).replace(" ", "")
        if not re.match(r'^(\+98|0)?9\d{9}$', phone):
            raise ValueError(_("Invalid phone number"))
        return phone
    


    def create_user(self, phone, password, **extra_fields):

        if not phone:
            raise ValueError(_("the phone must be set"))
        
        
        
        phone = self.phone_validate(phone)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))

        return self.create_user(phone, password, **extra_fields)
