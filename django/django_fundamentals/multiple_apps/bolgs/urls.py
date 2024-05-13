from django.urls import path,include
from . import views

app_name = 'bolgs_app'
urlpatterns = [
    path('',views.index,name="index"),
    path('new',views.new,name="new"),
    path('create',views.create,name="create"),
    path('<int:number>',views.show,name="show"),
    path('<int:number>/edit',views.edit,name="edit"),
    path('<int:number>/delete',views.destroy,name="delete"),
]