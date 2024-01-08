from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls', namespace='users')),
    path('', include('pdf_reader.urls', namespace='pdf_reader')),
    path('',include('pdf_utilits.urls', namespace='pdf_utilits')),
    path('',include('image_to_doc.urls', namespace='image_to_doc')),
    path('api/', include('core.urls', namespace='core')),
]
