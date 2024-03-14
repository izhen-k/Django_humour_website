from django import forms
from django.core.exceptions import ValidationError

from .models import Category,Table
import re

# class TableForm(forms.Form):
#     title = forms.CharField(label="Название", widget=forms.TextInput(attrs={'class':'form-control'}), max_length=150)
#     content = forms.CharField(label='Содержание', widget=forms.TextInput(attrs={'class':'form-control', 'rows':5}))
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', widget=forms.Select(attrs={'class':"form-control"}))
#     is_published = forms.BooleanField(initial=True, label='Опубликовать')
#     photo = forms.ImageField

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['title','content','category','is_published','photo']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control', 'rows':5}),
            'category':forms.Select(attrs={'class':"form-control"}),
            'photo':forms.FileInput(attrs={'class':'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d',title):
            raise ValidationError('Пошел нахер с цифры начинать!')
        return title

