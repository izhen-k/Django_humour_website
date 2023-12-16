from project.views import zero_page,news
from django.urls import path

urlpatterns = [
    path('studyproject/', zero_page),
    path('news/', news)
]