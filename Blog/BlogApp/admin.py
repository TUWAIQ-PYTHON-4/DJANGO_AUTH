from django.contrib import admin
from .models import Post, Comments


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'date', 'image',)
    list_filter = ('user', 'date',)
    search_fields = ('user',)


class CommentsAdmin(admin.ModelAdmin):
    first_name = ('first_name', 'email', 'content', 'date', 'post',)
    list_filter = ('first_name', 'date',)
    search_fields = ('first_name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)
