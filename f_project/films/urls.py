from django.urls import path, include, re_path

from films import views

urlpatterns = [
    # 注册
    path('index/', views.index, name='index'),

]