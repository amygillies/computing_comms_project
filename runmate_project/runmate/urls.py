from django.conf.urls import url
from runmate import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.dataView, name='data view')
]
