from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index),
    path("guess",views.guess),
    path("play_again",views.play_again),
    path('save_winner',views.save_winner),
    path('show',views.show)
   # path('admin/', admin.site.urls),
]
