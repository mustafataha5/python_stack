from django.urls import path,include
from . import views

app_name = 'users_app'
urlpatterns = [
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('users/new',views.new,name="new"),
    path('users/',views.index,name="index"),
    path('',views.root,name="root"),
]