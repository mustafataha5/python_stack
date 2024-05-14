from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addUser',views.add_user)
]
