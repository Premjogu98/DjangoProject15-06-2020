# Generated by Django 3.0.6 on 2020-05-14 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_trending_design'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(default='', max_length=50)),
                ('Last_name', models.CharField(default='', max_length=50)),
                ('Username', models.CharField(default='', max_length=15)),
                ('Email_Phone', models.CharField(default='', max_length=15)),
                ('Password', models.CharField(default='', max_length=15)),
            ],
        ),
    ]