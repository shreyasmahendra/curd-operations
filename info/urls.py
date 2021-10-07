from . import views
from django.urls import path

urlpatterns =[
    path('',views.operation, name='operation'),
    path('product/', views.product, name="product"),
    path('productList/', views.productList, name="productList"),
    path('edit/<int:user_id>/', views.edit, name= 'edit'),
    path('update/<int:user_id>/', views.update, name="update"),
    path('delete/<int:user_id>/', views.delete, name="delete"),
    path('product/get/', views.pedit, name ="edit"),
    path('product/get/id/<int:p_id>/', views.getproduct, name="getid"),
    path('product/update/', views.productupdate, name="updateproduct"),
    path('product/delete/<int:p_id>/', views.productdelete, name="deleteproduct"),
]
