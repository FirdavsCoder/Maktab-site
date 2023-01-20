from django.db import models

# Create your models here.

class raxbar(models.Model):
  direktor = models.CharField(max_length=45)
  yoordamchisi = models.CharField(max_length=45)
  madanyatchi = models.CharField(max_length=45)
  sekretar = models.CharField(max_length=45)

class Xaqida(models.Model):
  xonalar = models.CharField(max_length=10)
  oshxona = models.CharField(max_length=10)
  sport = models.CharField(max_length=10)
  malumot = models.CharField(max_length=100)

class News(models.Model):
  rasim = models.ImageField(upload_to='media')
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=1000)

class Talim(models.Model):
  rasimt = models.ImageField(upload_to='media')
  namet = models.CharField(max_length=100)
  titlet = models.CharField(max_length=500)

class Sharoyit(models.Model):
  rasims = models.ImageField(upload_to='media')
  names = models.CharField(max_length=100)
  titles = models.CharField(max_length=500)

class Murojat(models.Model):
  fish = models.CharField(max_length=100)
  otasi = models.CharField(max_length=100)
  onasi = models.CharField(max_length=100)
  rasim = models.ImageField(upload_to='media')
  malumot = models.TextField()
  raqam = models.CharField(max_length=12)
  vaqt = models.DateTimeField(auto_now=True)

class Dasturchi(models.Model):
  nnn = models.CharField(verbose_name="Ismi: ",max_length=200)
  rrr = models.ImageField(verbose_name="Rasmi: ",upload_to="media/photo")
  ttt = models.CharField(verbose_name="Telefon raqami: ", max_length=12)
  smm = models.CharField(verbose_name="Telegram: ", max_length=200)
  about = models.CharField(verbose_name="Qo'shimcha ma'lumotlar: ", max_length=500)

class Xodimlar(models.Model):
  ismit = models.CharField(verbose_name="Ismi va Familiyasi", max_length=80)
  rasmit = models.ImageField(verbose_name="Rasmi", upload_to="media/xodimlar")
  yoshi = models.BigIntegerField(verbose_name="Yoshi", null=False)
  fan = models.CharField(verbose_name="Fani", max_length=40, null=True)
  lavozimi = models.CharField(verbose_name="Lavozimi", max_length=90)
  about_data = models.CharField(verbose_name="Qo'shimcha malumotlar", max_length=400)
  tel_raqam = models.CharField(verbose_name="Telefon raqami", max_length=20)
