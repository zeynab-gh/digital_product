from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=50)
    description = models.CharField('description', max_length=250)
    avatar = models.ImageField(blank=True, upload_to='categories/')
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

    def __str__(self) -> str:
        return self.title

class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPE = (
        (FILE_AUDIO, 'audio'),
        (FILE_VIDEO, 'video'),
        (FILE_PDF, 'pdf'),
    )
    product = models.ForeignKey('Product', related_name='files', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=50)
    file_type = models.PositiveSmallIntegerField('file type', choices=FILE_TYPE)
    description = models.CharField('description', max_length=250)
    is_enable = models.BooleanField(default=True)
    file = models.FileField(upload_to='files')
    create_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self) -> str:
        return self.title