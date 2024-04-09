from django.db import models
from goods.models import Variant
from accounts.models import BaseUser
from django.utils import timezone

class Cart(models.Model):

    user = models.ForeignKey(BaseUser, verbose_name=' نام کاربر', on_delete=models.CASCADE, related_name='cart_user')
    create_at = models.DateTimeField(default=timezone.now())

class CartItem(models.Model):

    cart = models.ForeignKey(Cart, verbose_name=' لیست', on_delete=models.CASCADE, related_name='cart_items')
    variant =  models.ForeignKey(Variant, verbose_name='نام محصول', on_delete=models.CASCADE, related_name='cart_supply', unique=True)
    quantity = models.PositiveIntegerField(verbose_name='تعداد محصول')
    


    

