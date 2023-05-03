# Generated by Django 3.2.3 on 2023-05-01 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Address', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40)),
                ('second_name', models.CharField(blank=True, max_length=40)),
                ('voivodeship', models.CharField(blank=True, max_length=40)),
                ('nationality', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=40)),
                ('street', models.CharField(max_length=40)),
                ('house_number', models.IntegerField()),
                ('zip_code', models.CharField(max_length=15)),
                ('E_mail', models.CharField(max_length=50)),
                ('Phone_number', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Addresses', to='Address.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]