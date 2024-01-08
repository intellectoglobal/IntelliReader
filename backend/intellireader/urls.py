from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Oauth2 authentication
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls', namespace='users')),
    path('', include('pdf_reader.urls', namespace='pdf_reader')),
    path('',include('pdf_utilits.urls', namespace='pdf_utilits')),
    path('',include('image_to_doc.urls', namespace='image_to_doc')),
    path('api/', include('core.urls', namespace='core')),
]
