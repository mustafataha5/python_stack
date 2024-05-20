from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('createUser',views.create_user),
    path('loginUser',views.login_user),
    path('success',views.success),
    path('logout',views.logout)
]