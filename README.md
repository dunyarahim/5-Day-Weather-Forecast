# 5-Day Weather Forecast CLI

This Python script fetches a 5-day weather forecast for a specified city and state using the OpenWeatherMap API. It retrieves the geographical coordinates based on the city and state, then fetches the forecast data in 3-hour intervals and processes it to display daily summaries including average temperature and common weather conditions.

## Features

- Retrieves geographical coordinates for any U.S. city/state using OpenWeatherMap Geocoding API
- Fetches detailed 5-day / 3-hour interval forecast using OpenWeatherMap Forecast API
- Calculates daily average temperature
- Summarizes most common weather description per day
- Displays results in a clean terminal output

## Setup

To get started, make sure you have Python 3 installed and install the required library:

```bash
pip install requests

Usage:
python weather_forecast.py


