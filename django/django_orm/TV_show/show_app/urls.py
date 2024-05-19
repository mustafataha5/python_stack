from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('shows',views.show_all),
    path('shows/new',views.show_new),
    path('shows/create',views.create_show),
    path('shows/<int:id>',views.show_by_id),
    path('shows/<int:id>/edit',views.edit_show),
    path("shows/<int:id>/update",views.update_show),
    path('shows/<int:id>/destroy',views.destroy_show),
]