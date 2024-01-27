from django.shortcuts import render
from django.http import HttpResponse
from project.models import Table,Category
from pprint import pprint


# Create your views here.


# def zero_page(request):
#     data = Table.objects.all()
#     html_content = '<h1>Hello World</h1>'
#     for i in data:
#         title = i.title
#         paragraph = f'<p>{title}</p>'
#         html_content += paragraph
#     pprint(request.__dict__)
#     return HttpResponse(html_content)


def news(request):
    data_news = Table.objects.all()     #запрос в бд
    return render(request,template_name='project/main_page.html', context={'title':'сидит на сайте', 'data':data_news})


def categories(request,category_id):
    data_categories = Table.objects.filter(category_id=category_id)
    all_data_categories = Category.objects.all()
    return render(request,template_name='project/categories.html', context={'title':'Категории', 'data':data_categories, 'categories':all_data_categories, 'current_category':category_id})
