from django.urls import path, include
from blog.models import Post,Comment
from django.views.generic import (TemplateView, ListView)
from blog import views

app_name='blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.UpdatePostView.as_view(), name = 'post_edit')
]