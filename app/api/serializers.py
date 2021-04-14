from rest_framework import serializers

from .models import Car


class CarCreateSerializer(serializers.ModelSerializer):
    """ Serializer for car object"""

    class Meta:
        model = Car
        fields = ('id', 'make', 'color', 'production_year',
                  'avg_fuel_consumption_per_100km', 'max_passengers')
        read_only_fields = ('id',)


class CarSerializer(serializers.ModelSerializer):
    """ Serializer for car object"""

    class Meta:
        model = Car
        fields = ('__all__')
        read_only_fields = ('id',)
