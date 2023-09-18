from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.user_register, name="user_register"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('add_post/', views.add_post, name="add_post"),
    path('update_post/<int:id>/', views.update_post, name="update_post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
]
