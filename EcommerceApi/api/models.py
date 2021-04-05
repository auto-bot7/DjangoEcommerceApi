from django.db import models

# Create your models here.
class Category(models.Model):
    title= models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Book(models.Model):
    book_title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,related_name='books', on_delete= models.CASCADE)
    unique_no = models.IntegerField
    price = models.CharField(max_length=255)
    stock = models.IntegerField()
    description = models.TextField(max_length=255)
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.book_title

class Product(models.Model):
    
    name=models.CharField(max_length=255)
    product_tag = models.CharField(max_length=255)
    category = models.ForeignKey(Category,related_name='products', on_delete= models.CASCADE)
    price = models.CharField(max_length=255)
    stock = models.IntegerField()
    description = models.TextField(max_length=255)
    imageUrl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.name


