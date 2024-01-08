from core.models import Documents
from rest_framework import serializers

class DocSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Documents
        fields = ('__all__')