from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

df = spark.createDataFrame(
    [("A", "URLA", "ContentA"),  # create your data here, be consistent in the types.
     ("B", "URLB", "ContentB")],
    ["company", "url", 'content']  # add your column names here
)

df.show()