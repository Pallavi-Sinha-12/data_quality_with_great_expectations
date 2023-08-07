from pyspark.sql import SparkSession
from data_quality.DataQuality import DataQuality
from utils.utils import create_df_from_dq_results

spark = SparkSession.builder.appName("DataQuality").getOrCreate()

student_df = spark.createDataFrame([
    (1,"Ram","Kumar", "Maths"),
    (2,"Shyam","Kumar", "History"),
    (3,"Mohan", None , "Science"),
    (4,"Sohan","Singh", "Maths"),
    (5,"Rohini","Kumari", "Science"),
    (6,"Raj", "Kumar", "Maths"),
    (7,"Meena", None , "Hindi"),
    (8,"Rani", "Kumari", "Sanskrit")], ["roll_no", "first_name", "last_name", "subject"])

dq = DataQuality(student_df, "config/config.json")
dq_results = dq.run_test()

dq_df = create_df_from_dq_results(spark, dq_results)
dq_df.show()