import requests
city=input("Enter city name:").strip()
geo_url="https://geocoding-api.open-meteo.com/v1/search"
geo_res=requests.get(geo_url,params={"name":city,"count":1},timeout=10).json()
if not geo_res.get("results"):
    print("city not found.")
else:
    place=geo_res["results"][0]
    lat=place["latitude"]
    lon=place["longitude"]
    tz=place.get("timezone","auto")
    url="https://api.open-meteo.com/v1/forecast"
    params={
        "latitude":lat,
        "longitude":lon,
        "current":"temperature_2m,wind_speed_10m,relative_humidity_2m",
        "timezone":tz
      }
response=requests.get(url,params=params,timeout=10)
data=response.json()
current=data["current"]
print(f"Location: {place['name']},{place.get('country', '')}")
print("Time:",current["time"])
print("Temperature(C):",current["temperature_2m"])
print("Wind Speed(km/h):",current["wind_speed_10m"])
print("Humidity(%):",current["relative_humidity_2m"])