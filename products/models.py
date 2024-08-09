from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=50)
    description = models.CharField('description', max_length=250)
    avatar = models.ImageField(blank=True, upload_to='categories')
    is_enable = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title



class Product(models.Model):
    category = models.ManyToManyField('Category', blank=True)
    title = models.CharField('title', max_length=50)
    description = models.CharField('description', max_length=250)
    avatar = models.ImageField(blank=True, upload_to='products/')
    is_enable = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class File(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=50)
    description = models.CharField('description', max_length=250)
    is_enable = models.BooleanField(default=True)
    file = models.FileField(upload_to='files')
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        