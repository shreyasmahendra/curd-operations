from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login-page'),
    path('authenticate/',views.operations,name='operations'),
    path('logout/',views.logout,name='logout'),

]