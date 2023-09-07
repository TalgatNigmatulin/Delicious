from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from post.views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet)



urlpatterns = [
    path('addm/', admin.site.urls),
    path('products/', include('post.urls')), 
    path('auth/', include('rest_framework.urls')),
    path('coments/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )   