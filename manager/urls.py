from . import views
from django.urls import path

urlpatterns =[
    path('',views.department.as_view()),
    path('<int:d_id>/',views.department.as_view()),
    ]