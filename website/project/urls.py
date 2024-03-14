from project.views import News, categories, news_description, add_joke
from django.urls import path

urlpatterns = [
    path('', News.as_view(), name='main'),
    path('categories/<int:category_id>/', categories, name='categories'),
    path('news/<int:news_id>/', news_description, name='news_description'),
    path('add-joke/', add_joke, name='add_joke')
]