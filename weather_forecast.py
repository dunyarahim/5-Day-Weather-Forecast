import os
import requests
from datetime import datetime
from collections import defaultdict

API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_coordinates(city, state, country='US'):
    """Retrieves the latitude and longitude for the specified city and state."""
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]['lat'], data[0]['lon']
    else:
        print("Location not found.")
        return None, None

def get_forecast(lat, lon):
    """Gets the 5-day weather forecast for the given coordinates."""
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial'
    response = requests.get(url)
    return response.json()

def process_forecast(data):
    """Processes the forecast data to extract daily summaries."""
    daily_forecast = defaultdict(list)
    for entry in data['list']:
        date = entry['dt_txt'].split(' ')[0]
        temp = entry['main']['temp']
        weather = entry['weather'][0]['description']
        daily_forecast[date].append((temp, weather))
    
    print("\n5-Day Weather Forecast:\n")
    for date, values in daily_forecast.items():
        temps = [temp for temp, _ in values]
        descriptions = [desc for _, desc in values]
        avg_temp = sum(temps) / len(temps)
        common_desc = max(set(descriptions), key=descriptions.count)
        print(f"{date}: {common_desc.capitalize()}, Avg Temp: {avg_temp:.1f}°F")

def main():
    city = input("Enter city name: ")
    state = input("Enter state code (e.g., MD for Maryland): ")
    lat, lon = get_coordinates(city, state)
    if lat and lon:
        forecast_data = get_forecast(lat, lon)
        process_forecast(forecast_data)

if __name__ == "__main__":
    main()
