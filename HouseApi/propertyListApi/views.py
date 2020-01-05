# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from .models import PropertyList
from .serializer import PropertySerializer


def get_object(self, pk):
    try:
        return PropertyList.objects.get(pk=pk)
    except PropertyList.DoesNotExist:
        raise Http404

@api_view(['GET'])
def view_property_list(request):
    property_available = PropertyList.objects.all()
    serializers = PropertySerializer(property_available, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def add_property_list(request):
    serializer = PropertySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_property(request,pk):
    property_available = PropertyList.objects.get(pk=pk)
    serializer = PropertySerializer(property_available, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_property(self,pk):
    property_available = PropertyList.objects.get(pk=pk)
    property_available.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def Single_property(request,pk):
    property_available = PropertyList.objects.get(pk=pk)
    serializers = PropertySerializer(property_available, many=False)
    return Response(serializers.data)







