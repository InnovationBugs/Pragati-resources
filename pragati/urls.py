from django.conf.urls import url, re_path
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^about/$', views.about, name = 'about pragati'),
    url(r'^app_download/$', views.landing, name = 'App intro'),
    url(r'^process/$', views.feedback, name = 'feedback'),
]
