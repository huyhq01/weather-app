import requests
from typing import Optional, Tuple, Any


SEARCH_URL = "https://geocoding-api.open-meteo.com/v1/search"


def get_info(city_name: str) -> Tuple[Optional[dict[str, Any]], Optional[str]]:
    params: dict[str, Any] = {"name": city_name, 'count': 1}
    # Get response json
    try:
        response = requests.get(SEARCH_URL, params=params)
        response.raise_for_status()
        data = response.json()
        # Check if response is valid
        results = data.get('results')
        if not results:
            return None, "City not found"
        city = results[0]
        return {
            'lat': city.get('latitude'),
            'lon': city.get('longitude'),
            'name': city.get('name'),
            'country': city.get('country'),
        }, None
    except requests.exceptions.RequestException as e:
        print(f"Geo API error: {e}")
        return None, "Service unavailable"
    