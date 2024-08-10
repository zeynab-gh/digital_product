from rest_framework import serializers
from .models import Category, Product, File

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')

class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ('id','title', 'file', 'file_type')
        
    def get_file_type(self,obj):
        return obj.get_file_type_display()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=True)
    files = FileSerializer(many=True) 
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'avatar', 'category', 'files', 'url')

   