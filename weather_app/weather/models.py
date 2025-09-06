from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class WeatherData(models.Model):
    city = models.CharField(max_length=100)  
    temperature = models.FloatField()  
    cloud = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
