# Generated by Django 4.2.6 on 2024-01-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_imagem_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=255, verbose_name='Descrição'),
        ),
    ]