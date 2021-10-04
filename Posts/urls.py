from django.urls import path
from .views import addPost,PostView,listpost,likeView,PostDetail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('post/addpost',login_required(PostView,login_url='login'),name='add_post'),
    path('post/ajax/Post',login_required( addPost,login_url='login'), name='post_Post'),
    path('posts/all',login_required(listpost,login_url='login'),name='listall'),
    path('like/<int:pk>',login_required(likeView,login_url='login'),name='like_post'),
    path('post/<int:pk>',login_required(PostDetail.as_view(),login_url='login'),name='post_detail')
]