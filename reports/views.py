from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import WeatherReport
from .serializers import WeatherReportSerializer


'''
List and create weather reports.
Handles:
- GET /api/reports/?city=Delhi  -> list reports (optionally filtered by city)
- POST /api/reports/            -> create a new weather report
'''
class WeatherReportListCreate(generics.ListCreateAPIView):
    serializer_class = WeatherReportSerializer

    '''
    Return filtered reports by city if provided,
    otherwise return all reports.
    '''
    def get_queryset(self):
        city = self.request.query_params.get("city")
        if city:
            return WeatherReport.objects.filter(city__iexact=city)
        return WeatherReport.objects.all()

    '''
    Save the new weather report after validation.
    '''
    def perform_create(self, serializer):
        serializer.save()


'''
Retrieve, update, or delete a single weather report.
Handles:
- GET /api/reports/{id}/
- PUT /api/reports/{id}/
- PATCH /api/reports/{id}/
- DELETE /api/reports/{id}/
'''
class WeatherReportRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherReport.objects.all()
    serializer_class = WeatherReportSerializer


'''
Basic health check endpoint to confirm API is running.
'''
@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})
