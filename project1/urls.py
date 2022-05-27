from unicodedata import name
from django.urls import URLPattern, path
from django.views import View
from .views import startapp, startapp2 , storeapp,loginapp,contact, carts , prod,view,Home

urlpatterns = [
    path('' , startapp2),
    
    path('store/' , storeapp),
    path('login/' , loginapp),
    path('contact/' , contact),
    path('three/<posid>' , carts , name='Nposid'),
    path('product/<prod>' , prod , name='prod'),
    path('store/view/<viw>' , view,name='view'),
    path('Home/' , Home)
    
]