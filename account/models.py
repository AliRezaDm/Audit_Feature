from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        "نام کاربری",
        max_length=150,
        unique=True,
        help_text= "وارد تمودن نام کاربری الزامی ست. نام کاربری شامل حداکثر 150 حرف انگلیسی یا کارکتر های @/./+/-/_ می باشد",
        validators=[username_validator],
        error_messages={
            "unique": "این نام کاربری توسط شخص دیگری به کار گرفته شده است",
        },
    )
    first_name = models.CharField("نام ", max_length=150, blank=True)
    last_name = models.CharField("نام خانوادگی", max_length=150, blank=True)
    
   
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        




