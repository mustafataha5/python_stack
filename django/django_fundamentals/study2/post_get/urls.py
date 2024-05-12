from django.urls import path,include
from . import views 
urlpatterns = [
    path('',views.index),
    path('request',views.some_fun),
    #path('admin/', admin.site.urls),
]
