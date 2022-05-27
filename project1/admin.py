from django.contrib import admin
from .models import SendFree,Store,ProductSlider,StoreNav,TowImg,cart,SliderTitle,ChangeLogo,ForImgBottom,TowImg,contacts,Category
from .models import nav
from django.utils.translation import gettext as _


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ['pos','Title','slug','status']
    list_filter = ['status']
    search_fields = ['Title' , 'slug']
    prepopulated_fields = {'slug':('Title' , )}


class navs(admin.ModelAdmin):
    pass
class ProductSliderAdmin(admin.ModelAdmin):
    
    list_display = ['ProdTitle','ProdImg_tag','ProdPrice','times','categorys_to_str']
    list_filter = ['about' , 'ProdPrice' , 'times']
    search_fields = ['about' , 'ProdTitle' , 'ProdPrice']
    
    fieldsets = [
        ('عنوان محصول' , {'fields':['ProdTitle']}),
        ('درباره محصول مختصر' , {'fields' : ['ProdAbout']}),
        ('درباره محصول' , {'fields':['about']}),
        ('قیمت محصول' , {'fields':['ProdPrice']}),
        ('عکس محصول' ,   {'fields': ['ProdImg']}),
        ('دسته بندی ها' ,   {'fields': ['categorys']}),

        
    ]
    def categorys_to_str(self , obj):
        return ", ".join([categorys.Title for categorys in obj.categorys.all()])
    categorys_to_str.short_description = "دسته بندی"

   

class SliderT(admin.ModelAdmin):
     list_display = ['Date','SliderTitle_tag']
     fieldsets = [
    ('Images' , {'fields':['SliderImgs']})
     ]
class Logos(admin.ModelAdmin):
    
    list_display = ['ChangLogo_tag'] 
    fieldsets = [
    ('Change Logo' , {'fields':['Logo']}),
     ]
class ImgBottom(admin.ModelAdmin):
     list_display = ['dates','ForImgBottom_tag','ForImgBottom2_tag','ForImgBottom3_tag','ForImgBottom4_tag']
     fieldsets = [
    ('Image1' , {'fields': ['Img1']}),
    ('Image2' , {'fields': ['Img2']}),
    ('Image3' , {'fields': ['Img3']}),
    ('Image4' , {'fields': ['Img4']}),
    ('ImageBug' , {'fields': ['ImgOne']}),
     ]
class towimg(admin.ModelAdmin):
    list_display = ['TowImg1_tag','TowImg2_tag']
    fieldsets = [
        ('ImageOne' , {'fields': ['Imgone']}),
        ('ImageTow' , {'fields': ['Imgtow']}),
    ]

class contact(admin.ModelAdmin):
    fieldsets = [
        
        ('اضافه کردن آدرس' , {'fields': ['adress']}),
        ('اضافه کردن شماره موبایل' , {'fields': ['mobile']}),
        ('اضافه کردن ایمیل' , {'fields': ['email']}),
        ('اضافه کردن عنوان' , {'fields': ['ContactTitle']}),
        ('اضافه کردن توضیحات' , {'fields': ['ContactAbout']}),
        ('اضافه کردن پشت زمینه' , {'fields': ['ContImg']}),
        ('اضافه کردن لوگو' , {'fields': ['ContactLogo']}),
    ]
class stor(admin.ModelAdmin):
    pass

class storenav(admin.ModelAdmin):
    pass

class Cart(admin.ModelAdmin):
    fieldsets = [
        ('عنوان' , {'fields': ['CTitle']}),
        ('درباره محصول' , {'fields': ['CAbout']}),
        ('قیمت محصول' , {'fields': ['CPrice']}),
        ('عکس محصول' , {'fields': ['Cimg']})
    ]

class cars(admin.ModelAdmin):
    pass

admin.site.register(nav,navs)
admin.site.register(ProductSlider,ProductSliderAdmin)
admin.site.register(Store , stor)
admin.site.register(StoreNav,storenav)
admin.site.register(cart , Cart)
admin.site.register(SendFree,cars)
admin.site.register(SliderTitle , SliderT)
admin.site.register(ChangeLogo, Logos)
admin.site.register(ForImgBottom,ImgBottom)
admin.site.register(TowImg,towimg)
admin.site.register(contacts,contact)
admin.site.register(Category,CategoryAdmin)