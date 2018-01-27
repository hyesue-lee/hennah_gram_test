from django.contrib import admin
from .models import Image, Comment, Like

class ImageAdmin (admin.ModelAdmin):
    list_display = (
        'location' ,
        'caption',
        'created_by',
        'updated_at',
    )

# Register your models here.
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)
admin.site.register(Like)



