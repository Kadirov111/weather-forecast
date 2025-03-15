from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import WeatherData
from .serializers import WeatherDataSerializer

class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all().order_by('-recorded_at')
    serializer_class = WeatherDataSerializer

    @action(detail=False, methods=['get'], url_path='locations/(?P<location_id>\d+)')
    def by_location(self, request, location_id=None):
        queryset = WeatherData.objects.filter(location_id=location_id).order_by('-recorded_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response({'count': len(queryset), 'results': serializer.data})
