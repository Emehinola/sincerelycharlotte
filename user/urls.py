from django.conf.urls import url
from django.contrib.auth.urls import urlpatterns
from . import views

urlpatterns = [
    url(r'register/', views.register, name='register'),
    url(r'logout/', views.logout_request, name='logout'),
    url(r'', views.login_request, name='login')
]
