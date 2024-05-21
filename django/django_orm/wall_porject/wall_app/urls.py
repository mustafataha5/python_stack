from django.urls import path
from . import views 


app_name = "wall_app"
urlpatterns = [
    path('',views.index,name='index'),
    path('createUser',views.create_user),
    path('loginUser',views.login_user),
    path('logout',views.logout),
    path('wall',views.main_wall,name='main_page'),
    path('addPost',views.add_post),
    path('addComment/<int:postID>',views.add_comment),
    path('deletePost/<int:postID>',views.delete_post),
]