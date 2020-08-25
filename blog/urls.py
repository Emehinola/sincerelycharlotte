from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<id>\d+)$', views.single_blog, name='single-blog'),
    url(r'like/', views.like, name='like'),
    url(r'fetch/', views.get_like, name='get_like'),
    url(r'category/(?P<category>\w+)$', views.category, name='category'),
    url(r'^$', views.index, name='home'),
]