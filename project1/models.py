from modulefinder import STORE_NAME
from pyexpat import model
from time import timezone
from tkinter import TRUE
from unicodedata import name
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext as _
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    Title = models.CharField(max_length=100)
    status   = models.BooleanField(default=True,verbose_name='نماییش داده شود یا نه')
    slug    = models.SlugField(max_length=100 , unique=True)
    pos     = models.IntegerField(verbose_name='پوزشن')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['pos']
    def __str__ (self):
        return self.Title


class nav(models.Model):
    names = models.CharField(max_length=40)
    hrf   = models.CharField(max_length=40)
    class Meta:
        verbose_name = 'تغیر عنوان صفحه اصلی'
    
    def __str__(self):
        return self.names
        

class ProductSlider(models.Model):
    ProdTitle = models.CharField(max_length=250,verbose_name='نام محصول')
    ProdAbout = models.CharField(max_length=38,verbose_name='در باره محصول مختصر')
    ProdPrice = models.IntegerField(verbose_name='قیمت محصول')
    about     = models.TextField(verbose_name='در باره محصول کلی')
    ProdImg   = models.ImageField(upload_to='%y/%m/%d' , null=True , blank=True,verbose_name='تغیر یا اضافه کردن عکس محصول')
    times = models.DateTimeField(default=timezone.now,null=True,blank=True,verbose_name='تاریخ انتشار محصول')
    categorys = models.ManyToManyField(Category,verbose_name='دسته بندی ها')
    class Meta:
        verbose_name = 'تغیر و اضافه کردن محصول '

    
    def __str__ (self):
        return self.ProdTitle
    def ProdImg_tag(self):
        return format_html("<img width=90 src='{}' >".format(self.ProdImg.url))
    ProdImg_tag.short_description = 'عکس محصول'


class Store(models.Model):
    StoreName = models.CharField(max_length=20)
    StoreAbout = models.TextField(max_length=50)
    StoreAvg   = models.IntegerField()

    def __str__ (self):
        return self.StoreName


class StoreNav(models.Model):
    NavName = models.CharField(max_length=20)
    logo    = models.ImageField(upload_to='logo/',null=True , blank=True)
    hrf    = models.CharField(max_length=20,null=True,blank=True)
    class Meta:
        verbose_name = 'تغیر عنوان صفحه فروشگاه'

    def __str__(self):
        return self.NavName


class cart(models.Model):
    CTitle = models.CharField(_('عنوان'),max_length=10)
    CAbout = models.TextField(max_length=100,default='Enter Youer Text')
    CPrice = models.IntegerField()
    Cimg   = models.ImageField(upload_to='SliderCart/')

    def __str__ (self):
        return self.CTitle


class SendFree(models.Model):
    Cartitle = models.CharField(max_length=30)
    CarAbout = models.TextField(max_length=70)
    Carlogo  = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'تغیر خدمات ارسال'
    def __str__ (self):
        return self.Cartitle

    

class SliderTitle(models.Model):
    SliderImgs = models.ImageField(upload_to='sliders/')
    Date       = models.DateTimeField(default=timezone.now,null=True,blank=True)
    class Meta:
        verbose_name = 'اضافه کردن عکس به سلایدر اول صفحه'

    def SliderTitle_tag(self):
        return format_html("<img width=90 src='{}' >".format(self.SliderImgs.url))
    SliderTitle_tag.short_description = 'عکس'
class ChangeLogo(models.Model):
    Logo = models.ImageField(upload_to='Logo/')

    class Meta:
        verbose_name = 'تغیر لوگو در تمام صفحات'

    def ChangLogo_tag(self):
        return format_html("<img width=90 src='{}' >".format(self.Logo.url))
    ChangLogo_tag.short_description = 'لوگوی صفحه'

class ForImgBottom(models.Model):
    Img1 = models.ImageField(upload_to='ForImg/')
    Img2 = models.ImageField(upload_to='ForImg/')
    Img3 = models.ImageField(upload_to='ForImg/')
    Img4 = models.ImageField(upload_to='ForImg/')

    ImgOne = models.ImageField(upload_to='ForImg/')
    dates  = models.DateTimeField(default=timezone.now,null=True,blank=True)

    class Meta:
        verbose_name = 'تغیر یا اضافه کردن عکس به قسمت چهار عکس'
    def ForImgBottom_tag(self):
        return format_html("<img width=90 src='{}' >".format(self.Img1.url))
    ForImgBottom_tag.short_description = 'عکس شماره ۱'

    def ForImgBottom2_tag(self):
        return format_html("<img width=90 src='{}' >".format(self.Img2.url))
    ForImgBottom2_tag.short_description = 'عکس شماره ۲'

    def ForImgBottom3_tag(self):
        return format_html("<img width=90 src='{}' >".format(self.Img3.url))
    ForImgBottom3_tag.short_description = 'عکس شماره ۳'

    def ForImgBottom4_tag(self):
        return format_html("<img width=90 src='{}' >".format(self.Img4.url))
    ForImgBottom4_tag.short_description = 'عکس شماره ۴'



class TowImg(models.Model):
    Imgone = models.ImageField(upload_to='TowImg/')
    Imgtow = models.ImageField(upload_to='TowImg/')
    class Meta:
        verbose_name = 'تغیر دو عکس پایین صفحه'


    def TowImg1_tag(self):
        return format_html("<img width=90 src='{}' >".format(self.Imgone.url))
    TowImg1_tag.short_description = 'عکس'
    
    def TowImg2_tag(self):
        return format_html("<img width=90 src='{}' >".format(self.Imgtow.url))
    TowImg2_tag.short_description = 'عکس2'

class contacts(models.Model):
    adress = models.CharField(max_length=50, null=True,blank=True)
    mobile = models.CharField(max_length=50, null=True,blank=True)
    email = models.CharField(max_length=50, null=True,blank=True)
    ContactTitle = models.CharField(max_length=20, null=True,blank=True)
    ContactAbout = models.TextField(max_length=200, null=True,blank=True)
    ContImg = models.ImageField(upload_to='bg-contact/')
    ContactLogo = models.ImageField(upload_to='Logo/', null=True,blank=True)
    def __str__ (self):
        return self.adress

    class Meta:
        verbose_name = 'تغیر مشخصات صفحه در باره ما یا تماس با ما'
