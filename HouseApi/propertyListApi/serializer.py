from rest_framework import serializers
from .models import PropertyList


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyList
        fields = '__all__'

