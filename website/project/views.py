from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from project.models import Table,Category
from pprint import pprint
from .forms import TableForm
from django.views.generic import ListView


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


# def news(request):
#     data_news = Table.objects.filter(is_published=True)     #запрос в бд
#     return render(
#         request,
#         template_name='project/main_page.html',
#         context={'title': 'сидит на сайте', 'data': data_news}
#     )


class News(ListView):
    model = Table
    template_name = 'project/main_page.html'
    context_object_name = 'data'
    # extra_context = {'title':'Жопа'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Жопа'
        return context

    def get_queryset(self):
        return Table.objects.filter(is_published=True)


# def categories(request, category_id):
#     data_categories = Table.objects.filter(category_id=category_id)
#     return render(
#         request,
#         template_name='project/categories.html',
#         context={'title': 'Категории', 'data': data_categories, 'current_category': category_id}
#     )


class Categories(ListView):
    model = Table
    template_name = 'project/categories.html'
    context_object_name = 'data'

    def get_queryset(self):
        return Table.objects.filter(category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(id=self.kwargs['category_id']).title
        return context



def news_description(request, news_id):
    # news_object = Table.objects.get(id=news_id)
    news_object = get_object_or_404(Table, id=news_id)
    return render(request, template_name='project/news_description.html', context={'news_object': news_object})


def add_joke(request):
    if request.method == 'POST':
        form = TableForm(request.POST, request.FILES)
        if form.is_valid():
            # new_joke = Table.objects.create(**form.cleaned_data)
            new_joke = form.save()
            return redirect(new_joke)
    elif request.method == 'GET':
        form = TableForm()
    return render(request, template_name='project/add_joke.html', context={'form': form})
