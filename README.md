# Live Weather Checker

A Python CLI script that fetches current weather conditions for any city using the **Open-Meteo** Geocoding and Forecast APIs[cite: 7, 15].

## Features
- Prompts the user for a city name and resolves its coordinates (`latitude`, `longitude`) and `timezone`.
- Fetches current weather metrics (`temperature_2m`, `wind_speed_10m`, `relative_humidity_2m`).
- Prints the location, timestamp, temperature (°C), humidity (%), and wind speed (km/h).

## Setup & Usage

1. **Install dependencies:**
   ```bash
   pip install requests

2. **Run the script:**
   ```bash
   python weathers.py

3. **Enter a city name** when prompted (for example, `Hyderabad`)

## Tech Stack
- Python
- `requests`
- Open-Meteo APIs