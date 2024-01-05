from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls', namespace='users')),
    path('', include('pdf_reader_app.urls', namespace='pdf_reader')),
    path('',include('pdf_utilits_app.urls', namespace='pdf_utilits')),
    path('',include('image_to_doc_app.urls', namespace='image_to_doc')),
]
