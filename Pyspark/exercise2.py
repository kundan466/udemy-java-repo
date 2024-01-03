from pyspark.sql import SparkSession
spark=SparkSesssion.builder.appname('sol').getOrCreate()
df=spark.read.csv('walmart_stock.csv',header=True,inferSchema=True)
df.column
df.printSchema()
for row in df.head(5):
    print(row)
    print('\n')
df.describe().show()
