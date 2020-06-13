# Generated by Django 3.0.6 on 2020-06-13 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200613_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='clothing_size',
        ),
        migrations.AddField(
            model_name='product',
            name='clothing_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.ClothingSize'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='shoe_size',
        ),
        migrations.AddField(
            model_name='product',
            name='shoe_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.ShoeSize'),
        ),
    ]
