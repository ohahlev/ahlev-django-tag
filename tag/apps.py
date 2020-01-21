from django.apps import AppConfig
from . import __version__ as VERSION

class TagConfig(AppConfig):
    name = "tag"
    verbose_name = "Tag Management %s" % VERSION