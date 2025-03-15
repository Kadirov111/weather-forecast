from rest_framework import serializers
from .models import Forecast
from locations.models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

class ForecastSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='location', write_only=True
    )

    class Meta:
        model = Forecast
        fields = [
            'id', 'location', 'location_id', 'forecast_date',
            'temperature_min', 'temperature_max', 'humidity',
            'precipitation_probability', 'wind_speed', 'wind_direction', 'created_at'
        ]
