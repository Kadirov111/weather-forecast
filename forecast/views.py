from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Forecast
from .serializers import ForecastSerializer

class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all().order_by('-forecast_date')
    serializer_class = ForecastSerializer

    @action(detail=False, methods=['get'], url_path='locations/(?P<location_id>\d+)')
    def by_location(self, request, location_id=None):
        queryset = Forecast.objects.filter(location_id=location_id).order_by('-forecast_date')
        serializer = self.get_serializer(queryset, many=True)
        return Response({'count': len(queryset), 'results': serializer.data})
