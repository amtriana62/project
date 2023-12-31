# Generated by Django 4.2.5 on 2023-09-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hojitas', '0002_alter_hoja_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoja',
            name='nombre',
            field=models.CharField(default=None, max_length=100, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='hoja',
            name='precio',
            field=models.IntegerField(default=0, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='hoja',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
