from django.contrib import admin

from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug',)
    list_filter = ('title',)
    search_fields = ('content',)


admin.site.register(BlogPost, BlogAdmin)
