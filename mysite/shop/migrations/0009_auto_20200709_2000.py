# Generated by Django 3.0.7 on 2020-07-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alljewellerys'),
    ]

    operations = [
        migrations.AddField(
            model_name='alljewellerys',
            name='image1',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='alljewellerys',
            name='image2',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='alljewellerys',
            name='image3',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]
