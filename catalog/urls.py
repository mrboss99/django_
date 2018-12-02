from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/(?p<pk>\d+', views.BoolDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors')
]

urlpatterns += [
    url('accounts/', include('django.contrib.auth.urls')),

]
