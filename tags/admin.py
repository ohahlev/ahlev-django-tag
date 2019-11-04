from django.contrib import admin
from .models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_detail', 'date_created', 'last_updated']
    search_fields = ['name', 'detail']
    fieldsets = [
        ('NAME', {
            'fields': ['name'],
        }),
        ('DETAIL', {
            'fields': ['detail'],
        }),
    ]

admin.site.register(Tag, TagAdmin)
