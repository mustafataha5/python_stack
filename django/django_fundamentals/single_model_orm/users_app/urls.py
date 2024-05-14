from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addUser',views.add_user),
     path('edit/<int:id>',views.edit),
     path('editUser/<int:id>',views.editUser),
      path('delete/<int:id>',views.delete)
]
