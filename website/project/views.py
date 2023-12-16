from django.shortcuts import render
from django.http import HttpResponse
from project.models import Table
from pprint import pprint

# Create your views here.


def zero_page(request):
    data = Table.objects.all()
    html_content = '<h1>Hello World</h1>'
    for i in data:
        title = i.title
        paragraph = f'<p>{title}</p>'
        html_content += paragraph
    pprint(request.__dict__)
    return HttpResponse(html_content)


def news(request):
    data = Table.objects.all()     #запрос в бд
    return render(request,template_name='project/index.html', context={'title':'сидит на сайте', 'data':data})
