# Generated by Django 4.0.2 on 2022-02-07 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='Blank', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='Blank', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]