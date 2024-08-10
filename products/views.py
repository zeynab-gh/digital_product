from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category,Product,File
from .serializer import CategorySerializer,ProductSerializer,FileSerializer


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True ,context={'request':request})
        return Response(serializer.data)
    
class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context={'request':request})
        return Response(serializer.data)


class CategoryListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True ,context={'request':request})
        return Response(serializer.data)
    
class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context={'request':request})
        return Response(serializer.data)   


class FileListView(APIView):
    def get(self, request , product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True ,context={'request':request})
        return Response(serializer.data)


class FileDetailView(APIView):

    def get(self, request, product_pk, pk):
        try:
            f = File.objects.get(pk=pk, product_id=product_pk)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(f, context={'request':request})
        return Response(serializer.data) 