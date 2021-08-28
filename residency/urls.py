from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('neehome/', views.products),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('resident/', views.resident, name="resident"),
    path('report/', views.report, name="report"),


]