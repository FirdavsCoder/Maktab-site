from django.contrib import admin
from .models import raxbar,Xaqida,News,Talim,Sharoyit,Murojat, Dasturchi, Xodimlar
# Register your models here.

class Raxbaryat(admin.ModelAdmin):
    list_display = ['id','direktor','yoordamchisi','madanyatchi','sekretar']

admin.site.register(raxbar,Raxbaryat)

class Xona(admin.ModelAdmin):
    list_display = ['id','xonalar','oshxona','sport','malumot']

admin.site.register(Xaqida,Xona)

class Newse(admin.ModelAdmin):
    list_display = ['id','rasim','name','title']

admin.site.register(News,Newse)

class Talims(admin.ModelAdmin):
    list_display = ['id','rasimt','namet','titlet']

admin.site.register(Talim,Talims)

class Qulay(admin.ModelAdmin):
    list_display = ['id','rasims','names','titles']

admin.site.register(Sharoyit,Qulay)

class Royxat(admin.ModelAdmin):
    list_display = ['id','fish','otasi','onasi','rasim','malumot','raqam','vaqt']

admin.site.register(Murojat,Royxat)

class Programmer(admin.ModelAdmin):
    list_display = ['id', "nnn", "rrr", "ttt", "smm", "about"]

admin.site.register(Dasturchi,Programmer)
admin.site.register(Xodimlar)

