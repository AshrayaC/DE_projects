# **Spark Streaming Twitter Sentiment Analysis**

This project is a **real-time sentiment analysis** of Twitter tweets using **Apache Kafka** and **Apache Spark Streaming**. The goal is to stream live Twitter data, analyze the sentiment of the tweets, and process the data in real-time.

### **Prerequisites**
Before you start, make sure you have the following installed:

1. **Java 8 or higher** (Required for Apache Spark and Kafka)
   - [Install Java](https://openjdk.java.net/install/)
2. **Apache Spark** (For streaming and processing data)
   - [Download Spark](https://spark.apache.org/downloads.html)
3. **Apache Kafka** (For real-time data streaming)
   - [Install Kafka](https://kafka.apache.org/quickstart)
4. **Python 3.x** (For the Python implementation)
   - [Download Python](https://www.python.org/downloads/)
5. **PySpark** (Python API for Apache Spark)
   - Install via pip: `pip install pyspark`
6. **Tweepy** (For Twitter API interaction)
   - Install via pip: `pip install tweepy`
7. **Git** (For version control)
   - [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
8. **Xcode** (Required for compiling dependencies on macOS)

### **Setup Instructions**

1. **Clone the repository**:

   Clone the project to your local machine using Git:

   ```bash
   git clone https://github.com/AshrayaC/DE_projects.git
   cd DE_projects
   ```

2. **Install Required Libraries**

   Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Twitter API Keys**

   To get access to Twitter's API, create a Twitter Developer Account and generate API keys. Follow the instructions on Twitter's Developer Platform to create an application and get the keys.

   After generating the keys, create a `.env` file in the project root with the following content:

   ```bash
   CONSUMER_KEY=your_consumer_key
   CONSUMER_SECRET=your_consumer_secret
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   ```

### **How It Works**

1. **Kafka Producer**: Fetches live tweets from the Twitter API using Tweepy and sends them to a Kafka topic.
2. **Spark Streaming Consumer**: A Spark Streaming job reads data from the Kafka topic in real-time, processes the tweet text, and performs sentiment analysis using a basic sentiment analysis model.
3. **Output**: The sentiment analysis results are displayed or stored in a specified format (CSV, database, etc.).

### **Running the Project**

Once everything is set up, follow these steps:

1. **Start Kafka**

   Make sure your Kafka server is running.

   ```bash
   # Start Zookeeper
   bin/zookeeper-server-start.sh config/zookeeper.properties

   # Start Kafka
   bin/kafka-server-start.sh config/server.properties
   ```

2. **Run the Kafka Producer**

   Run the Twitter streaming producer to fetch tweets and send them to Kafka:

   ```bash
   python spark_streaming/twitter_producer.py
   ```

3. **Start Spark Streaming Job**

   To start processing the real-time tweets, run the Spark Streaming job:

   ```bash
   spark-submit --master local[2] --jars /path/to/kafka-clients.jar /path/to/spark_streaming_twitter.py
   ```

4. **Monitor the Output**

   The Spark job will continuously process tweets and output sentiment analysis results to the console or a database.

### **Project Structure**

```
DE_projects/
│
├── README.md               # Project overview and setup instructions
├── spark_streaming/        # Contains Spark Streaming job files
│   ├── twitter_producer.py
│   ├── spark_streaming_twitter.py
├── requirements.txt        # Python dependencies
└── .env                    # Twitter API keys (do not commit to GitHub)
```


