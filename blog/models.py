from django.db import models

# Create your models here.



class Fruit(models.Model):
    name = models.CharField(max_length=200, null = True , blank= True)
    price = models.CharField(max_length=20, null = True , blank= True)
    available = models.CharField(max_length=20, null = True , blank= True)
    description = models.TextField(null = True , blank= True)
    image = models.ImageField(upload_to='images/', verbose_name=('Image'), blank=True, null=True)
    STATUS_CHOICE = (
        ('m' , 'موجود'),
        ('n','ناموجود')
    )
    status = models.CharField(max_length=1,choices=STATUS_CHOICE)


    def __str__(self):
        return self.name



class Vegtabale(models.Model):
    name = models.CharField(max_length=200, null = True , blank= True)
    price = models.CharField(max_length=20, null = True , blank= True)
    available = models.CharField(max_length=20, null = True , blank= True)
    description = models.TextField(null = True , blank= True)
    image = models.ImageField(upload_to='images/', verbose_name=('Image'), blank=True, null=True)
    STATUS_CHOICE = (
        ('m' , 'موجود'),
        ('n','ناموجود')
    )
    status = models.CharField(max_length=1,choices=STATUS_CHOICE)


    def __str__(self):
        return self.name