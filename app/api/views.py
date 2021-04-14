from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Car
from .serializers import CarSerializer, CarCreateSerializer


class CarViewSet(viewsets.ViewSet):

    def list(self, request):
        cars = Car.objects.all()
        ser = CarSerializer(cars, many=True)
        return Response(ser.data)

    def retrieve(self, request, pk=None):
        cars = Car.objects.all()
        car = get_object_or_404(cars, pk=pk)
        ser = CarSerializer(car)
        return Response(ser.data)

    def create(self, request):
        ser = CarCreateSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
