from django.contrib import admin
from .models import Category,File,Product

#admin.site.register(File)
#admin.site.register(Product)
#admin.site.register(Category)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =[ 'parent','title', 'is_enable', 'create_time']
    list_filter =['is_enable', 'parent']
    search_fields = ['title']

class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file', 'is_enable']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['title', 'is_enable', 'create_time']
    list_filter =['is_enable']
    search_fields = ['title']
    filter_horizontal = ['category']
    inlines = [FileInLineAdmin]
