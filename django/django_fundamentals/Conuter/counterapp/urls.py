from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index),
    path('destroy_session',views.destroy_session),
     path('add_two',views.add_two),
     path('add_n',views.add_n),
    #path('admin/', admin.site.urls),
]