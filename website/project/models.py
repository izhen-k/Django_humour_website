from django.db import models

# Create your models here.
class Table(models.Model):
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-created_at']
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано в')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено в')
    photo = models.ImageField(null=True, blank=True, verbose_name='Фотография')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return self.title



class Category(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

