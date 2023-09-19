from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('addm/', admin.site.urls),
    path('products/', include('post.urls')), 
    path('auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )   