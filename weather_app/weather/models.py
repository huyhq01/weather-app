from django.db import models


class LocationReference(models.Model):
    name = models.CharField(max_length=100)
    name_no_sign = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"


class WeatherDescription(models.Model):
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)


# class HistorySearch(models.Model):
#     name = models.CharField(max_length=100)
#     name_no_sign = models.CharField(max_length=100)
    

class WeatherDaily(models.Model):
    location = models.ForeignKey(LocationReference, on_delete=models.CASCADE, related_name='weather_daily')
    date = models.DateField()
    temperature_max = models.FloatField()
    temperature_min = models.FloatField()
    weather_code_day = models.ForeignKey(WeatherDescription, on_delete=models.PROTECT, related_name='weather_in_day')
    weather_code_evening = models.ForeignKey(WeatherDescription, on_delete=models.PROTECT, related_name='weather_in_night')
    updated_at = models.DateTimeField(auto_now=True)


class WeatherHourly(models.Model):
    day = models.ForeignKey(WeatherDaily, on_delete=models.CASCADE, related_name='weather_hourly')
    hour = models.IntegerField()
    temperature_2m = models.FloatField()  # Nhiệt độ không khí ở độ cao 2 mét
    relative_humidity_2m = models.IntegerField()  # Độ ẩm ở độ cao 2 mét
    precipitation_probability = models.IntegerField()  # Khả năng mưa
    wind_speed_10m = models.FloatField()  # Tốc độ gió ở độ cao 10 mét
    weather_code = models.ForeignKey(WeatherDescription, on_delete=models.PROTECT, related_name='weather_in_hour')

