from rest_framework import serializers
from .models import AnimalTest

class AnimalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalTest
        fields = '__all__'