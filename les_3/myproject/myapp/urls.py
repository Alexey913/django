from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('random/<str:kind>/<int:count>/', views.rand, name='rand'),
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),
]