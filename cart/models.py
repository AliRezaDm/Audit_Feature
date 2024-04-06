from django.db import models
from django.utils import timezone
from goods.models import Supply
from accounts.models import BaseUser


class Cart(models.Model):

    user = models.ForeignKey(BaseUser, verbose_name='کاربر', on_delete=models.CASCADE)
    product = models.ForeignKey(Supply, verbose_name="محصول", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='تعداد', default=1)
    create_time = models.DateTimeField(verbose_name='زمان ثبت', default=timezone.now())
    customer_name = models.CharField(max_length=150, verbose_name='نام مشتری', blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    # def get_absolute_url(self):
    #     return reverse("cart:cart_detail")


