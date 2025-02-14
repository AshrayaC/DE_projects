from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from textblob import TextBlob
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("TwitterSentiment").getOrCreate()

# Read from Kafka
tweets_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "twitter_stream")
    .load()
)

# Convert Kafka value to string
tweets_df = tweets_df.selectExpr("CAST(value AS STRING)")

# Define Sentiment Analysis UDF
def get_sentiment(text):
    analysis = TextBlob(text)
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"

sentiment_udf = udf(get_sentiment, StringType())

# Apply Sentiment Analysis
tweets_df = tweets_df.withColumn("sentiment", sentiment_udf(col("value")))

# Write output to console (or DB)
query = (
    tweets_df.writeStream
    .outputMode("append")
    .format("console")  # Use "jdbc" for database
    .start()
)

query.awaitTermination()