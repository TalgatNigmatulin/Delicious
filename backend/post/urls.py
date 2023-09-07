from django.urls import path
from . import views





urlpatterns = [
    path('', views.ProductsList .as_view(), name='post_list'),
    path('<slug:slug>/', views.ProductDetail.as_view(), name='post_detail'),

    path('burgery/', views.ProductsList.as_view()),
    path('pizza/', views.ProductsList.as_view()),
    path('deserty/', views.ProductsList.as_view()),
    path('sushi-i-rolly/', views.ProductsList.as_view()),
    path('salaty/', views.ProductsList.as_view()),
    path('zakusky/', views.ProductsList.as_view()),
   
    

    
]
