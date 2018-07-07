from django.conf.urls import url, re_path
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
]
