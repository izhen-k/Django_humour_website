from django.contrib import admin

# Register your models here.
from project.models import Table
from project.models import Category


class TableAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'is_published', 'views', 'category')
    list_editable = ('is_published',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('is_published', 'views', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Table, TableAdmin)
admin.site.register(Category, CategoryAdmin)