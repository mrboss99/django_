from django.urls import path
from django.conf.urls import url

from catalog import views

urlpatterns = [
    path('', views.Index.as_view(), name='index')
]