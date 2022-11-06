from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug:slug>/', views.detail, name='blog_detail')
]
