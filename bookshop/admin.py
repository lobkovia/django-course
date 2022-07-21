from django.contrib import admin
from . import models


admin.site.index_title = 'Мой охуенный заголовок'
admin.site.site_header = 'Админка'

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','rating','is_best_selling']
    list_editable = ['rating', 'is_best_selling']
