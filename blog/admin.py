from django.contrib import admin
from .models import  *
# Register your models here.


class FruitAdmin(admin.ModelAdmin):
    list_display = ('name','id','price','available','status')
    list_filter = ('status','price')
    search_fields = ('name','description','price')


class VegtabaleAdmin(admin.ModelAdmin):
    list_display = ('name','id','price','available','status')
    list_filter = ('status','price')
    search_fields = ('name','description','price')



admin.site.register(Fruit, FruitAdmin)
admin.site.register(Vegtabale, VegtabaleAdmin)