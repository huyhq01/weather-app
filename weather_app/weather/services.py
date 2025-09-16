import requests
from typing import Any
from .models import WeatherDescription, WeatherDaily, WeatherHourly, LocationReference
from datetime import datetime
from .serializers import WeatherDailySerializer
from django.core.cache import caches


JSON_TYPE = dict[str, Any]
# SEARCH_URL = "https://geocoding-api.open-meteo.com/v1/search"
GET_WEATHER_DATA_URL = "https://api.open-meteo.com/v1/forecast"
HOURLY_FIELDS = [
    "temperature_2m",  # Nhiệt độ
    "relative_humidity_2m",  # Độ ẩm %
    "precipitation_probability",  # Khả năng mưa %
    "wind_speed_10m",  # Tốc độ gió km/h
    "weather_code",  # Mã thời tiết
]


def fetch_weather_data(lat: float, lon: float) -> JSON_TYPE:
    params: JSON_TYPE = {
        "latitude": lat,
        "longitude": lon,
        "hourly": ",".join(HOURLY_FIELDS),
    }
    response = requests.get(GET_WEATHER_DATA_URL, params=params)
    response.raise_for_status()
    return response.json()


def get_weather_data(name_no_sign: str, day_index: int = 0):
    # check location is valid
    if not is_location_valid(name_no_sign): 
        print("location not found")
        return None

    # format input name for cache key
    name_no_sign_cache = name_no_sign.strip().replace(' ', '_')
    
    #  get cache first if exists
    data = get_caches(f"{name_no_sign_cache}_day{day_index}")
    if data: 
        print("cache found")
        return data

    # get response from api then take main data in hourly
    location = LocationReference.objects.get(name_no_sign=name_no_sign)
    weather_data = fetch_weather_data(location.latitude, location.longitude)['hourly']

    # save data
    # TODO: save_history_location() for user logged in only
    weather_daily: list[WeatherDaily] = save_weather_daily(location, weather_data)
    save_weather_hourly(weather_daily, weather_data)

    # set cache then return data from cache
    save_weather_to_caches(name_no_sign_cache, weather_daily)
    print("cache not found")
    return get_caches(f'{name_no_sign_cache}_day{day_index}')


# def save_history_location(location_data: JSON_TYPE):
#     location, is_created = HistorySearch.objects.update_or_create(
#         name_no_sign = location_data.get("name_no_sign"),
#         defaults={
#             "name": location_data.get("name"),
#         },
#     )
#     print("save location info", location, is_created)
#     return location


def save_weather_daily(location: LocationReference, weather_data: JSON_TYPE):
    weather_daily: list[WeatherDaily] = []
    # take the first hours of each day 0 - 24 - 48
    for i in range(0, len(weather_data["time"]), 24):
        # get date as yyyy-mm-dd
        target_date = datetime.fromisoformat(weather_data["time"][i]).strftime(
            "%Y-%m-%d"
        )
        # get temp
        temp_in_day = weather_data["temperature_2m"][i : i + 24]
        temperature_max, temperature_min = max(temp_in_day), min(temp_in_day)
        # get weather code
        list_code: list = weather_data["weather_code"][i : i + 24]
        code_day = max(list_code[6:13], key=list_code[6:13].count)
        code_evening = max(list_code[13:21], key=list_code[13:21].count)
        # create record
        weather_in_day = {
            "date": target_date,
            "temperature_max": temperature_max,
            "temperature_min": temperature_min,
            "weather_code_day": WeatherDescription.objects.get(code=code_day),
            "weather_code_evening": WeatherDescription.objects.get(code=code_evening),
        }
        # save record to db only when both location and date is matched
        day, _ = WeatherDaily.objects.update_or_create(
            location=location, date=target_date, defaults=weather_in_day
        )
        weather_daily.append(day)
        # print("save days: ", day.date, is_created)
    return weather_daily


def save_weather_hourly(weather_daily: list[WeatherDaily], weather_data: JSON_TYPE):
    count_created = 0
    count_updated = 0
    # first_day = []
    # loop through 7 days then slice weather_data and loop each 24 hours
    # hour is the index of each sliced array
    for i, day in enumerate(weather_daily):
        for hour, j in enumerate(range(i * 24, (i + 1) * 24)):
            weather_hour = {
                "temperature_2m": weather_data["temperature_2m"][j],
                "relative_humidity_2m": weather_data["relative_humidity_2m"][j],
                "precipitation_probability": weather_data["precipitation_probability"][j],
                "wind_speed_10m": weather_data["wind_speed_10m"][j],
                "weather_code": WeatherDescription.objects.get(code=weather_data["weather_code"][j])
            }
            _, is_created = WeatherHourly.objects.update_or_create(
                day = day,
                hour = hour,
                defaults = weather_hour
            )
            if is_created: count_created += 1
            else: count_updated += 1
            # if i==0: first_day.append(day)


def is_location_valid(name_no_sign: str):
    return LocationReference.objects.filter(name_no_sign=name_no_sign).exists()


def save_weather_to_caches(name_no_sign: str, weather_daily: list[WeatherDaily]):
    for i in range(0, len(weather_daily)):
        value = WeatherDailySerializer(weather_daily[i]).data
        set_caches(f'{name_no_sign}_day{i}', value, timeout=30*60)


def set_caches(key: str, value: Any, timeout: int):
    caches["default"].set(key, value, timeout=timeout)


def get_caches(key: str):
    return caches["default"].get(key)