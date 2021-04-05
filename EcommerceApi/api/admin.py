from django.contrib import admin
from .models import Category, Book, Product
# Register your models here.



@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display=['title']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=[ 'id','book_title','category','unique_no', 'price', 'stock','description','imageUrl', 'status', 'date_created']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id', 
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

    