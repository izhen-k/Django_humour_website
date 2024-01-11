from project.views import news,categories
from django.urls import path

urlpatterns = [
    path('', news, name='main'),
    path('categories/<int:category_id>', categories, name='categories')
]