from django.conf.urls import url
from . import views

app_name = "tag"
urlpatterns = [
    url('', views.index, name='index'),
]


