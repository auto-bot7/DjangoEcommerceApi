from rest_framework import serializers
from .models import Category,Book,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
        'id',
        'book_title',
        'category',
        'unique_no',
        'price',
        'stock',
        'description',
        'imageUrl',
        'status',
        'date_created'
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
        'id', 
        'name',
        'product_tag'
        ,'category'
        ,'price'
        ,'stock',
        'description'
        ,'imageUrl'
        ,'status'
        ,'date_created'
        ]



