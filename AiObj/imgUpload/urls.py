from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.imageUpload,name = 'imageUpload'),
    url(r'imageprocess',views.imageprocess,name='imageprocess')
]
