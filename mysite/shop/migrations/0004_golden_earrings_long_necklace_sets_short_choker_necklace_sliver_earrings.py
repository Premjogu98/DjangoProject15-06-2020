# Generated by Django 3.0.6 on 2020-05-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_semi_bridal_sets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Golden_Earrings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(default='', max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Long_Necklace_Sets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(default='', max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Short_Choker_Necklace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(default='', max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Sliver_Earrings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(default='', max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/images')),
            ],
        ),
    ]
