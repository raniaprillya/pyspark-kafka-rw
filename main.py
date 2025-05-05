from pyspark.sql import SparkSession

## Create a spark session
spark = SparkSession.builder \
    .appName("KafkaIntegration") \
    .config("spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0,"
            "com.clickhouse:clickhouse-jdbc:0.4.6") \
    .getOrCreate()


from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as F
import json
from pyspark.sql.functions import *
from pyspark.sql.types import StringType, StructField, StructType, ArrayType, LongType
import clickhouse_connect
import pandas as pd


spark = SparkSession.builder \
    .appName("KafkaExample") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "spark-kafka-trial") \
    .load()

df_1 = df.selectExpr("cast(value as string) as value")

df_schema = StructType([
    StructField("id", DecimalType()),
    StructField("name", StringType()),
    StructField("value", DecimalType()),
    StructField("date", DateType()),
])

df_2 = df_1.withColumn("value", from_json(df_1.value, df_schema)).select("value.*")

df_2.writeStream \
  .format("console") \
  .option("truncate", "false") \
  .outputMode("append") \
  .start() \
  .awaitTermination()
