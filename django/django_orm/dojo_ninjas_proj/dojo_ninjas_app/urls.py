#from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('addDojo',views.add_dojo),
    path('addNinja',views.add_ninja),
   # path('admin/', admin.site.urls),
]
