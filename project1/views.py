from django.shortcuts import render
from django.http import HttpResponse
from .models import SendFree, ProductSlider, nav, Store,StoreNav, cart,SliderTitle,ChangeLogo,ForImgBottom,TowImg,contacts

# Create your views here.


def startapp(request):
    return HttpResponse('<h1>milad</h1>')


def startapp2(request):
    logo = ChangeLogo.objects.all()[1:]
    hnav = nav.objects.all()
    Car = SendFree.objects.all()[:4]
    dbs = ProductSlider.objects.all()
    dbs_filt = ProductSlider.objects.all()[7:]
    Cart = cart.objects.all()
    Slidertitle = SliderTitle.objects.all()
    img4 = ForImgBottom.objects.all()
    towimg = TowImg.objects.all()[:2]
    contex = {
        'filt':dbs_filt,
        'num':dbs,
        'nav':hnav,
        'crt':Cart,
        'car':Car,
        'slider':Slidertitle,
        'logoss':logo,
        'img4':img4,
        'towimg':towimg,
    }
    return render(request , 'project1/index.html' , contex)





def storeapp(request):
    Connect_Store = ProductSlider.objects.all()
    Connect_StoreNav = StoreNav.objects.all()
    logo  = ChangeLogo.objects.all()[1:]
    stores = {
        'store':Connect_Store,
        'storenav': Connect_StoreNav,
        'logo':logo,
    }
    return render(request , 'project1/store/store.html' , stores)    

def loginapp(request):
    return render(request, 'project1/login/index.html')

def contact(request):
    conts = contacts.objects.all()
    CContaxe = {
        'conts':conts,
    }
    return render(request , 'project1/contact-me/contact.html',CContaxe)


def carts(request , posid):
    post = cart.objects.get(id=posid)
    changelogo = ChangeLogo.objects.all()[:1]
    Pcontax = {
        'post':post,
        'logo':changelogo
        
    }
    return render(request , 'project1/index2.html' , Pcontax)


def prod(request,prod):
    prods = ProductSlider.objects.get(id=prod)
    ProdContax = {
        'prod':prods
    }
    return render(request , 'project1/prod.html',ProdContax)


def view(request , viw):
    viewe = ProductSlider.objects.get(id=viw)
    vcontax = {'view':viewe}
    return render(request , 'project1/view.html',vcontax)

def footer(request):
    conts = contacts.objects.all()
    CContaxe = {
        'conts':conts,
    }
    return render(request , 'project1/footer.html',CContaxe)

def Home(request):
    
    dbs = ProductSlider.objects.all()
    contax = {
        'dbs':dbs,
    }
    return render(request , 'project1/home.html' ,contax)