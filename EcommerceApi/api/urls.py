from django.urls import path,include
from .views import CategoryView, BookView,ProductView
from rest_framework.routers import DefaultRouter
from api import views

router= DefaultRouter()

router.register('category', views.CategoryView, basename = 'categorys')
router.register('book', views.BookView, basename = 'bookg')
router.register('product', views.ProductView, basename = 'producta')



urlpatterns = [
    path('', include(router.urls))
]
