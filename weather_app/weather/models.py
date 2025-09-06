from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()  # Nhiệt độ không khí ở độ cao 2 mét
    relative_humidity_2m = models.IntegerField()  # Độ ẩm
    precipitation_probability = models.IntegerField()  # Khả năng mưa
    wind_speed_10m = models.FloatField()  # Tốc độ gió ở độ cao 10 mét
    weather_code = models.IntegerField()  # Mã thời tiết, mô tả
    created_at = models.DateTimeField(auto_now_add=True)
