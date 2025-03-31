import requests
from kafka import KafkaProducer
import json
import time

# Kafka Configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Convert dict to JSON bytes
)

# Weather API URL (New York example)
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&current_weather=true"

def fetch_weather():
    """Fetch real-time weather data."""
    response = requests.get(WEATHER_API_URL)
    if response.status_code == 200:
        return response.json()["current_weather"]
    else:
        return {"error": "Failed to fetch weather"}

# Produce Live Weather Data
for _ in range(10):  # Fetch and send 10 times
    weather_data = fetch_weather()
    producer.send('weather_data', weather_data)
    print(f"✅ Sent: {weather_data}")
    time.sleep(5)  # Fetch new data every 5 seconds

producer.close()
print("✅ Producer finished sending weather updates!")
