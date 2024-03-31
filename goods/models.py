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


class Supply(models.Model):

    STATUS_CHOICE = (
        ('A', 'موجود' ),  
        ('N', 'ناموجود')
    )   

    
    id = models.BigAutoField(verbose_name='شناسه محصول', primary_key=True)
    image = models.ImageField(verbose_name='تصویر محصول', upload_to='media', null=True)
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='cat')
    title = models.CharField(max_length=100, verbose_name='نام محصول')
    color = models.ManyToManyField('Color' ,related_name='goods', verbose_name='رنگ', null=True, blank=True)
    size = models.ManyToManyField('Size', related_name='goods', verbose_name='اندازه', null=True, blank=True)
    status = models.CharField(max_length=1, verbose_name='وضعیت محصول', choices=STATUS_CHOICE)
    count = models.IntegerField(verbose_name='تعداد')

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
    
    def colors_to_str(self):
          return " - ".join([color.name for color in self.colors.all()])
    colors_to_str.short_description = 'رنگ ها'

    def sizes_to_str(self):
        return " - ".join([size.name for size in self.sizes.all()])
    sizes_to_str.short_description = 'اندازه ها'

    def get_absolute_url(self):
        return reverse("goods:supply_list")
    


class Color(models.Model):
    
    name = models.CharField('نام رنگ', max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
      
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'


class Size(models.Model):
    
    name = models.CharField('عنوان اندازه', max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        
        verbose_name = 'اندازه'
        verbose_name_plural = 'اندازه ها'