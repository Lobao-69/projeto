# Generated by Django 5.0.1 on 2024-01-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Imagem do Produto'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='Preço do Produto'),
        ),
    ]
