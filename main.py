from pyspark.sql import SparkSession
from data_quality.DataQuality import DataQuality
from utils.utils import create_df_from_dq_results

spark = SparkSession.builder.appName("DataQuality").getOrCreate()

student_df = spark.createDataFrame([
    (1, "Maths"),
    (2, "History"),
    (3, "Science"),
    (4, "Maths"),
    (5, "Science"),
    (6, "Maths"),
    (7, "Hindi"),
    (8, "Sanskrit")], ["roll_no", "subject"])

dq = DataQuality(student_df, "config/config.json")
dq_results = dq.run_test()

dq_df = create_df_from_dq_results(spark, dq_results)
dq_df.show()