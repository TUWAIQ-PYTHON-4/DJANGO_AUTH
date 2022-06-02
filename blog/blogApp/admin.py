from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('post','date')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)


# Register your models here.
