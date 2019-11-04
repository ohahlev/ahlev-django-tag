from django.conf.urls import url
from . import views

app_name = "tags"
urlpatterns = [
    url('', views.index, name='index'),
]


