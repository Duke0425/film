from django.urls import path, include, re_path

from films import views

urlpatterns = [
    # 电影
    path('category_movies/', views.category_movies, name='category_movies'),

]