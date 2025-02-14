from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Initialize the Spark session with Kafka package
spark = SparkSession.builder \
    .appName("KafkaTwitterStream") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2") \
    .getOrCreate()

# Set log level to reduce unnecessary logs
spark.sparkContext.setLogLevel("WARN")

# Read the Kafka stream
kafka_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "AI") \
    .load()

# Convert the binary "value" column to a string (tweets are encoded in byte format)
tweets = kafka_stream.selectExpr("CAST(value AS STRING) as tweet")

# Show tweets on the console
query = tweets.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Await termination of the query
query.awaitTermination()
