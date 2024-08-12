from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
    path('services/', views.sservices, name='services'),
    path('profile/<str:userid>/', views.profile, name='profile'),
    path('saving_rel/<str:userid>/', views.saving, name='saving'),
    path('remove_rel/<str:serviceid>/', views.remove, name='remove_service'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.register_user, name='signup'),
    path('add-service/', views.add_service, name='add-service'),
    path('see-closer/<str:id>', views.see_closer, name='see-closer'),
    path('delete_service/<str:serviceid>', views.delete_service, name='delete'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_comment/<str:id>', views.delete_comment, name='delete_comment'),


]
""" path('profile/<str:userid>/my_services', views.myservices, name='myservices')"""
