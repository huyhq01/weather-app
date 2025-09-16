from rest_framework import serializers
from .models import (
    WeatherDaily,
    WeatherHourly,
)


class WeatherHourlySerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    
    def get_description(self, obj):
        return obj.weather_code.description
    
    class Meta:
        model = WeatherHourly
        fields = (
            "hour",
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation_probability",
            "wind_speed_10m",
            "description",
        )


class WeatherDailySerializer(serializers.ModelSerializer):
    # location_name = serializers.SerializerMethodField()
    day_description = serializers.SerializerMethodField()
    night_description = serializers.SerializerMethodField()
    weather_hourly = WeatherHourlySerializer(many=True, read_only=True)

    # def get_location_name(self, obj):
    #     return obj.location.name

    def get_day_description(self, obj):
        return obj.weather_code_day.description

    def get_night_description(self, obj):
        return obj.weather_code_evening.description

    class Meta:

        model = WeatherDaily
        fields = (
            # "location_name",
            "date",
            "temperature_max",
            "temperature_min",
            "day_description",
            "night_description",
            "weather_hourly",
        )
