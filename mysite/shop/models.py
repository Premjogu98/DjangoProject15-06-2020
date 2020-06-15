from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default='')
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/images', default='')

    def __str__(self):
        return self.product_name


class Semi_Bridal_Sets(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default='')
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/images', default='')

    def __str__(self):
        return self.product_name


class Short_Choker_Necklace(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default='')
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/images', default='')

    def __str__(self):
        return self.product_name


class Long_Necklace_Sets(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default='')
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/images', default='')

    def __str__(self):
        return self.product_name


class Sliver_Earrings(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default='')
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/images', default='')

    def __str__(self):
        return self.product_name


class Golden_Earrings(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default='')
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/images', default='')

    def __str__(self):
        return self.product_name


class Trending_design(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default='')
    pub_date = models.DateField()
    image = models.ImageField(upload_to='static/images', default='')

    def __str__(self):
        return self.product_name


class user(models.Model):
    First_name = models.CharField(max_length=50, default='')
    Last_name = models.CharField(max_length=50, default='')
    Username = models.CharField(max_length=15, default='')
    Email_Phone = models.CharField(max_length=15, default='')
    Password = models.CharField(max_length=15,default='')

    def __str__(self):
        return self.Username



