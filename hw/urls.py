from django.urls import path
from .views import (
    home, create_homework, edit_homework, hw_delete,
    profile_list, profile_create, profile_edit, profile_delete,
    comment_list, create_comment, edit_comment, comment_delete
)

urlpatterns = [
    # Homework URLs
    path('', home, name='home'),
    path('homework/create/', create_homework, name='create_homework'),
    path('homework/edit/<int:id>/', edit_homework, name='edit_homework'),
    path('homework/delete/<int:id>/', hw_delete, name='hw_delete'),

    # Profile URLs
    path('profiles/', profile_list, name='profile_list'),
    path('profiles/create/', profile_create, name='profile_create'),
    path('profiles/edit/<int:id>/', profile_edit, name='profile_edit'),
    path('profiles/delete/<int:id>/', profile_delete, name='profile_delete'),

    # Comment URLs
    path('comments/', comment_list, name='comment_list'),
    path('comments/create/', create_comment, name='create_comment'),
    path('comments/edit/<int:id>/', edit_comment, name='edit_comment'),
    path('comments/delete/<int:id>/', comment_delete, name='comment_delete'),
]
