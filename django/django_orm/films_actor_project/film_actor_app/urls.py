from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index),
    path('movies',views.index2),
     path('movie/<int:id>',views.show_movie),
    path('actors',views.show_all_actors),
]