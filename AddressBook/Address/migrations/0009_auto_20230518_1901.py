# Generated by Django 3.2.3 on 2023-05-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0008_alter_voivodeship_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voivodeship',
            options={'ordering': ('name',), 'verbose_name_plural': 'Voivodeships'},
        ),
        migrations.AlterField(
            model_name='address',
            name='E_mail',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='address',
            name='nationality',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='voivodeship',
            name='name',
            field=models.CharField(choices=[('MAŁOPOLSKIE', 'MAŁOPOLSKIE'), ('ŚLĄSKIE', 'ŚLĄSKIE'), ('LUBUSKIE', 'LUBUSKIE'), ('WIELKOPOLSKIE', 'WIELKOPOLSKIE'), ('ZACHODNIOPOMORSKIE', 'ZACHODNIOPOMORSKIE'), ('DOLNOŚLĄSKIE', 'DOLNOŚLĄSKIE'), ('OPOLSKIE', 'OPOLSKIE'), ('KUJAWSKO-POMORSKIE', 'KUJAWSKO-POMORSKIE'), ('POMORSKIE', 'POMORSKIE'), ('WARMIŃSKO-MAZURSKIE', 'WARMIŃSKO-MAZURSKIE'), ('ŁÓDZKIE', 'ŁÓDZKIE'), ('ŚWIĘTOKRZYSKIE', 'ŚWIĘTOKRZYSKIE'), ('LUBELSKIE', 'LUBELSKIE'), ('PODKARPACKIE', 'PODKARPACKIE'), ('PODLASKIE', 'PODLASKIE'), ('MAZOWIECKIE', 'MAZOWIECKIE'), ('FOREIGNER/CUDZOZIEMIEC', 'FOREIGNER/CUDZOZIEMIEC')], max_length=40),
        ),
    ]