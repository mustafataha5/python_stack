from django.urls import path #,include
from . import views

app_name="gold"
urlpatterns = [
    path("",views.index,name='index'),
    path("set_attr",views.set_attr),
    path("gold",views.gold,name='gold_page'),
    path("process_money/<str:from_which>",views.process,name='process'),
    path("reset",views.reset,name='reset'),
    path("show",views.show)
    #path('admin/', admin.site.urls),
]
