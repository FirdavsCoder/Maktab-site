# Generated by Django 4.1.4 on 2023-01-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0015_xodimlar'),
    ]

    operations = [
        migrations.AddField(
            model_name='xodimlar',
            name='about_data',
            field=models.CharField(default=12, max_length=400, verbose_name="Qo'shimcha malumotlar"),
            preserve_default=False,
        ),
    ]
