from kafka import KafkaConsumer
import json

# Kafka Configuration
consumer = KafkaConsumer(
    'weather_data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='weather_consumer_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Convert bytes to dict
)

print("⏳ Waiting for weather updates...")

for msg in consumer:
    print(f"📥 Received: {msg.value}")
