# Generated by Django 4.1.2 on 2023-01-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0007_alter_murojat_rasim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='murojat',
            name='rasim',
            field=models.ImageField(upload_to='media'),
        ),
    ]
