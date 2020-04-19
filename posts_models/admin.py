from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created_at', 'author')
    search_fields = ('text',)
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
