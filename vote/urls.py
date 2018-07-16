from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^tv/$', views.tv),
    url(r'^viral/$', views.viral),
    url(r'^exit/$', views.exit),
    url(r'^result/$', views.result),
]
