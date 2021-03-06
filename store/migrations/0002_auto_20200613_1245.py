# Generated by Django 3.0.6 on 2020-06-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='clothing_size',
        ),
        migrations.AddField(
            model_name='product',
            name='clothing_size',
            field=models.ManyToManyField(blank=True, null=True, to='store.ClothingSize'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='shoe_size',
        ),
        migrations.AddField(
            model_name='product',
            name='shoe_size',
            field=models.ManyToManyField(blank=True, null=True, to='store.ShoeSize'),
        ),
    ]
