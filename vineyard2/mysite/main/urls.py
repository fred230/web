from django.urls import path

from . import views 

urlpatterns = [ 
path ("", views.index, name = "index"),
path ('prayer_post/', views.prayer_post, name = "prayer"),
path ('prayer_success/', views.prayer_success, name = "prayer_success"),

path ('contact/', views.contact, name = "contact"),
path ('addblogpost/', views.addBlogPost, name = "addblogpost"),
path ('about/', views.about, name = "about"),
path ('blog/', views.blog.as_view(), name = "blog"),
path ('<slug:slug>/', views.blog_single.as_view(), name = "blog_single"),
path ('article/edit/<int:pk>/', views.editBlogPost.as_view(), name = "editblogpost"),

path ('article/<int:pk>/remove', views.deleteBlogPost.as_view(), name = "deleteblogpost"),





]