# Generated by Django 4.2.5 on 2023-09-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hojitas', '0003_hoja_nombre_hoja_precio_alter_hoja_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoja',
            name='precio',
            field=models.PositiveIntegerField(default=0, verbose_name='Precio'),
        ),
    ]
