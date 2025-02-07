# Spark Streaming with Kafka - Twitter Sentiment Analysis

This project demonstrates how to use Spark Streaming and Kafka for real-time sentiment analysis of tweets. The goal is to collect tweets from Twitter in real-time using Kafka, process the data using Spark Streaming, and perform sentiment analysis on the tweets.

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Java**:
   - Install Java 11 or higher.
   - You can install Java via Homebrew:
     ```bash
     brew install openjdk@11
     ```

2. **Apache Spark**:
   - Install Apache Spark with:
     ```bash
     brew install apache-spark
     ```

3. **Apache Kafka**:
   - Install Apache Kafka using Homebrew:
     ```bash
     brew install kafka
     ```

4. **Python & PySpark**:
   - Install Python (Python 3.x recommended).
   - Install PySpark:
     ```bash
     pip install pyspark
     ```

5. **Twitter API Access**:
   - You'll need to have access to the Twitter API. Create a Twitter Developer account and create an app to get the necessary API keys.

6. **Kafka Topics**:
   - You need to create a Kafka topic to send and receive messages. Use the following commands to create the topic:
     ```bash
     kafka-topics --create --topic twitter-stream --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
     ```

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/spark_streaming_kafka.git
cd spark_streaming_kafka