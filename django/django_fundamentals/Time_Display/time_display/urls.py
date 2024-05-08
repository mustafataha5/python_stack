from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('time_display',views.display),
    path('clock',views.display2),
 #   path('admin/', admin.site.urls),
]
