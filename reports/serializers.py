from rest_framework import serializers  

# Importing the WeatherReport model

from .models import WeatherReport

# Serializer for WeatherReport model


class WeatherReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherReport
        fields = "__all__"



"class WeatherReportCreateSerializer(serializers.ModelSerializer):"
