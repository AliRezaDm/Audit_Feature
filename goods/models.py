from django.db import models
from django.utils import html 
from django.urls import reverse

#Managers
class SupplyManager(models.Manager):
     
     def Available(self):
          return Supply.objects.filter(status='A')


class Category(models.Model):

    id = models.BigAutoField(verbose_name='شناسه دسته', primary_key=True)
    parent = models.ForeignKey('self', default=None, null=True, blank=True,\
             on_delete=models.SET_NULL, related_name='children', verbose_name='زیردسته')
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی‍')
    status = models.BooleanField(default=True, verbose_name='وضعیت نمایش')



    class Meta:
            verbose_name = 'دسته بندی '
            verbose_name_plural = 'دسته بندی ها '

    def __str__(self):
         return self.title
    
    def get_absolute_url(self):
        return reverse("goods:category_list")

class Supply(models.Model):

    STATUS_CHOICE = (
        ('A', 'موجود' ),  
        ('N', 'ناموجود')
    )   

    image = models.ImageField(verbose_name='تصویر محصول', upload_to='media', null=True)
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='cat')
    title = models.CharField(max_length=100, verbose_name='نام محصول')
    status = models.CharField(max_length=1, verbose_name='وضعیت محصول', choices=STATUS_CHOICE)
    description = models.TextField(verbose_name="توضیحی درباره محصول", blank=True, null=True)

    #initializing the manager
    objects = SupplyManager()


    class Meta:
    
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def __str__(self):
         return self.title
    
    def image_tag(self):
         return html.format_html("<img width=100; height=75; style='border-radius:10px;'src='{}'>".format(self.image.url))
    image_tag.short_description = short_decsription = 'تصویر محصول'

    def get_absolute_url(self):
        return reverse("goods:supply_list")
    


class Color(models.Model):
    
    name = models.CharField('نام رنگ', max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
      
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'

    def get_absolute_url(self):
        return reverse("goods:supply_list")

class Size(models.Model):
    
    name = models.CharField('عنوان اندازه', max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        
        verbose_name = 'اندازه'
        verbose_name_plural = 'اندازه ها'

    def get_absolute_url(self):
        return reverse("goods:supply_list")
    


class Variant(models.Model):
         
    supply=models.ForeignKey(Supply, verbose_name='نام محصول', on_delete=models.CASCADE, related_name='variant_supply')
    color=models.ForeignKey(Color, verbose_name='رنگ محصول', on_delete=models.CASCADE, related_name='variant_color')
    size=models.ForeignKey(Size, verbose_name='سایز محصول', on_delete=models.CASCADE, related_name='variant_size')
    count=models.PositiveIntegerField(verbose_name='تعداد', default=0)

    def __str__(self):
        return self.supply.title 

    def __unicode__(self):
        return 'supply id: {}'.format(self.supply.id)