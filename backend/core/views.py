from core.serializer import DocSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Documents


class DocPost(viewsets.ViewSet):
    queryset = Documents.objects.all()

    def create(self, request):
        serializer_class = DocSerializer(self.queryset, many = True)
        return Response(serializer_class.data)
