from django.contrib import admin
from .models import Category, News


# admin.site.register(Category)
# admin.site.register(News)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']


admin.site.site_header = "Miracle Admin"
admin.site.site_title = "Miracle Admin Portal"
admin.site.index_title = "Welcome to Miracle News Portal"
