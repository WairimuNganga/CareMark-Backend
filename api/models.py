from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from api.manager import CustomUserManager

PHONE_NUMBER_REGEX = RegexValidator(
    r"(254|0)(1|7)([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])",
    "Phone number should be in the format 254712234345",
)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phonenumber = models.CharField(validators=[PHONE_NUMBER_REGEX], max_length=12)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


def upload_to(instance,filename):
    return 'blister_image_id{0}'.format(filename)

class ImageVerification(models.Model):
    patient = models.ForeignKey('User', on_delete=models.PROTECT, related_name='blister_image_id_patient')
    blister_image_url = models.ImageField(("blister_image_url"),upload_to=upload_to,default = '')
    timestamp = models.DateTimeField()    
