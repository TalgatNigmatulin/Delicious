from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'comments', views.CommentViewSet)


urlpatterns = [
    path('', views.ProductsList .as_view(), name='post_list'),
    path('<slug:slug>/<int:pk>/', views.ProductDetail.as_view(), name='post_detail'),
    path('burgery/', views.ProductsList.as_view()),
    path('pizza/', views.ProductsList.as_view()),
    path('deserty/', views.ProductsList.as_view()),
    path('sushi-i-rolly/', views.ProductsList.as_view()),
    path('salaty/', views.ProductsList.as_view()),
    path('zakusky/', views.ProductsList.as_view()),
    path('coments/', include(router.urls)),
    

    
]


