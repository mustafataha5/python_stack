from django.urls import path
from . import views


app_name = 'book'
urlpatterns = [
    path('',views.index,name='index'),
    path('reg&login',views.registeration_and_login,name='reg&login'),
    path('createUser',views.create_user),
    path('loginUser',views.login_user),
    path('logout',views.logout),
    path('mainPage',views.main_page,name='main_page'),
    path('addBook',views.add_book),
    path('book/<int:bookID>',views.book),
    path('book/<int:bookID>/edit',views.edit_book,name='edit'),
    path('book/<int:bookID>/delete',views.delete_book,name='delete'),
    path('deleteUserFromBook/<int:bookID>',views.delete_user_from_book),
    #path('book/<int:bookID>/show',views.show_book,name="show"),
    path('addFaveriteBook',views.add_faverite_book),
    
]