from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('login/',views.Login.as_view()),
    path('logout/',views.logout),
    path('signup/',views.Signup.as_view()),

]
