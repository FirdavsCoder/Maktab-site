from django.shortcuts import render
from .models import raxbar,Xaqida,News,Talim,Sharoyit,Murojat, Dasturchi, Xodimlar
import datetime
# Create your views here.

def home(malumot):
  raxbarlar = raxbar.objects.all()
  xona = Xaqida.objects.all()
  news = News.objects.all().order_by('-id')[:1]
  talim = Talim.objects.all().order_by('-id')[:1]
  sharoit = Sharoyit.objects.all().order_by('-id')[:1]
  dasturchi = Dasturchi.objects.all().order_by('-id')[:1]


  if malumot.method == "POST":
    fish = malumot.POST.get('name')
    otasi = malumot.POST.get('otasi')
    onasi = malumot.POST.get('onasi')
    rasim = malumot.POST.get('img')
    qoshimcha = malumot.POST.get('qoshimcha')
    raqam = malumot.POST.get('phone-number')
    vaqt = datetime.datetime.now()
    Murojat(fish=fish,otasi=otasi,onasi=onasi,rasim=rasim,malumot=qoshimcha,raqam=raqam,vaqt=vaqt).save()

  return render(malumot, 'index.html', {'raxbar':raxbarlar, 'xonalar': xona, 'newse':news,'talim':talim,'sharoit': sharoit, 'dasturchi':dasturchi})

def news(malumot):
  raxbarlar = raxbar.objects.all()
  xona = Xaqida.objects.all()
  news = News.objects.all().order_by('-id')
  talim = Talim.objects.all().order_by('-id')[:1]
  sharoit = Sharoyit.objects.all().order_by('-id')[:1]
  dasturchi = Dasturchi.objects.all().order_by('-id')[:1]

  return render(malumot, 'news.html',  {'raxbar':raxbarlar, 'xonalar': xona, 'newse':news,'talim':talim,'sharoit': sharoit, 'dasturchi':dasturchi})

def dasturchi(malumot):
  raxbarlar = raxbar.objects.all()
  xona = Xaqida.objects.all()
  news = News.objects.all().order_by('-id')
  talim = Talim.objects.all().order_by('-id')[:1]
  sharoit = Sharoyit.objects.all().order_by('-id')[:1]
  dasturchi = Dasturchi.objects.all().order_by('-id')[:1]
  return render(malumot, 'dasturchi.html',  {'raxbar':raxbarlar, 'xonalar': xona, 'newse':news,'talim':talim,'sharoit': sharoit, 'dasturchi':dasturchi})

def xodimlar(malumot):
  raxbarlar = raxbar.objects.all()
  xona = Xaqida.objects.all()
  news = News.objects.all().order_by('-id')
  talim = Talim.objects.all().order_by('-id')[:1]
  sharoit = Sharoyit.objects.all().order_by('-id')[:1]
  dasturchi = Dasturchi.objects.all().order_by('-id')[:1]
  xodimlar = Xodimlar.objects.all().order_by('-id')
  return render(malumot, 'xodimlar.html',  {'raxbar':raxbarlar, 'xonalar': xona, 'newse':news,'talim':talim,'sharoit': sharoit, 'dasturchi':dasturchi, 'xodimlar':xodimlar})

