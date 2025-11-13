from django.urls import path
from .views import home, create_homework, edit_homework, hw_delete, profile_list, profile_create, profile_edit, profile_delete

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_homework, name='create_homework'),
    path('edit/<int:id>/', edit_homework, name='edit_homework'),
    path('delete/<int:id>/', hw_delete, name='hw_delete'),


    #for profile
    path('', profile_list, name='profile_list'),
    path('create/', profile_create, name='profile_create'),
    path('edit/<int:id>/', profile_edit, name='profile_edit'),
    path('delete/<int:id>/', profile_delete, name='profile_delete'),
]
