from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [('Date Information', {'fields' : ['publish_date'], 'classes' : ['collapse']})]

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'time']