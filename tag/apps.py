from django.apps import AppConfig
from django.utils.html import format_html
from . import __version__ as VERSION

class TagConfig(AppConfig):
    name = 'tag'
    verbose_name = format_html("Tag Management <span class='version'>{}</span>", VERSION)
