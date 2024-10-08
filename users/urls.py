from django.urls import path
from . import views

app_name="users"

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('create/', views.create, name='createProfile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('favorites_list/', views.favorites_list, name='favorites_list'),
    path('favorite/<int:id>', views.favorite, name="favorite"),
    path('delete_favorite/', views.delete_favorite, name='delete_favorite'), 
    path('save_favorite/', views.save_favorite, name="save_favorite"),
]
