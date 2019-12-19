from django.contrib import admin
from .models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_created', 'last_updated', 'preview_type', 'type', 'preview_detail']
    search_fields = ['name', 'detail']
    """
    class Media:
        css = {
        'all': (
            'css/fontawesome.css',
            'css/bootstrap.min.css',
            'css/mdb.min.css',
            'css/mystyle.css'
            )
         }
        js = (
            'js/jquery.min.js', 
            'js/popper.min.js',
            'js/bootstrap.min.js',
            'js/mdb.min.js',
            'js/myscript.js'
        )
    """
admin.site.register(Tag, TagAdmin)
