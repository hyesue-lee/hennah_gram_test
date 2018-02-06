from django.contrib import admin
from .models import Image, Comment, Like

class ImageAdmin (admin.ModelAdmin):


    list_display = (
        'location' ,
        'caption',
        'created_by',
        'updated_at',
    )
  
    search_fields = (
        'location',
       
    )
    list_display_links = (
        'caption',
        
    )

    list_filter = (
        'created_at',
        'location',
        'created_by',
        
    )

    ordering = (
        'created_at',
        'updated_at',
    )

class CommentAdmin (admin.ModelAdmin):
    list_display = (
        'message',
        'created_by',
        'created_for',
        'updated_at',
        'created_at',
    )
    list_display_links = (
        'created_for',
        'message',
    )    
    list_filter = (
        'message',
        'updated_at',
        'created_at',
    )    

    search_fields = (
        'message',
        'updated_at',
        'created_at',
    )
  
# Register your models here.
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)




