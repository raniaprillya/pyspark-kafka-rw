# 📡 Kafka to ClickHouse Real-Time Streaming with PySpark

This PySpark application performs **real-time streaming from Apache Kafka to ClickHouse**, enabling scalable ingestion and processing of event-driven data pipelines.

---

## 🚀 Features

- ✅ Reads streaming data from a Kafka topic using **Spark Structured Streaming**
- ✅ Writes processed data directly into **ClickHouse** via JDBC
- ✅ Supports high-throughput, low-latency ingestion workflows
- ✅ Designed for real-time analytics, monitoring, or ETL pipelines

---

## ⚙️ Technologies Used

- Apache Kafka
- Apache Spark (Structured Streaming)
- ClickHouse (columnar OLAP database)
- PySpark (Python API for Apache Spark)
- ClickHouse JDBC driver (via `spark.jars.packages`)
- Kafka topic with JSON-formatted messages

---

## 🛠️ Prerequisites

- A running Kafka broker (with at least one configured topic)
- A running ClickHouse server with a target table
- Apache Spark 3.x installed with Python 3.x
- Network access from Spark to Kafka and ClickHouse
- ClickHouse JDBC driver: `com.clickhouse:clickhouse-jdbc:0.4.6`

---

## 🧪 Sample Kafka Message Format 

```json
{"id": "10", "name": "Alice", "value": "10.9", "date":"2023-10-28"}
```

---

## Clickhouse create table query

```sql
CREATE TABLE example_table (
  id Int,
  name String,
  value String,
  date DateTime
) ENGINE = MergeTree()
ORDER BY id;
```
