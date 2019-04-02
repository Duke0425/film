<<<<<<< HEAD
from django.urls import path, include

from users import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('index/', views.index, name='index'),
]
=======
from django.urls import path, include, re_path

from users import views

# urlpatterns = [
#     # 注册
#     path('register/', views.register, name='register'),
#     # 登录
#     path('login/', views.login, name='login'),
# ]
>>>>>>> 477b48fbd1757348f95819fb7f034b01a7973b9b
