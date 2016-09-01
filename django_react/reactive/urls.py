from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^api/$', views.api, name='api'),
	url(r'^kanban/$', views.kanban, name='kanban')
]