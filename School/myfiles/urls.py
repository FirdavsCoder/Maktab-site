from django.urls import path
from .views import news, home, dasturchi, xodimlar

urlpatterns = [
    path('', home, name = 'home'),
    path('news/', news, name='news'),
    path('dasturchi/', dasturchi, name = "dasturchi"),
    path('xodimlar/', xodimlar, name='xodimlar')
]