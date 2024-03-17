from django.db import models

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
    image = models.ImageField(verbose_name='تصویر محصول', upload_to='media')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='cat')
    title = models.CharField(max_length=100, verbose_name='نام محصول')
    status = models.CharField(max_length=1, verbose_name='وضعیت محصول', choices=STATUS_CHOICE)
    count = models.IntegerField(verbose_name='تعداد')

    #initializing the manager
    objects = SupplyManager()


    class Meta:
    
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
         return self.title
