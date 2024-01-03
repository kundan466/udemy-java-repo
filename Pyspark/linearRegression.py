from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql.functions import corr

spark=SparkSesssion.builder.appname('cruise').getOrCreate()
df=spark.read.csv('cruise_ship_info.csv',header=True,inferSchema=True)
indexer=StringIndexer(inputCol='Cruise_line',outputCol='crew')
indexer=indexer.fit(df).transform(df)
assembler=VectorAssembler(inputCols=['Age',
                                    'Tonnage',
                                    'length',
                                    'cabins',
                                    'passenger_density',
                                    'cruise_cat'],outputCol='features')
output=assembler.transform(indexed)
output.select('features','crew').show()
final_data=output.select('[features','crew'])
train_data,test_data=final_data.randomSplit([0.7,0.3])
ship_lr=LinearRegression(labelCol='crew')
trained_ship_model=ship_lr.fit(train_data)
ship_results=trained_ship_model.evaluate(test_data)

ship_results.rootmeanSquaredError //0.6720
ship_results.r2 //0.9560
ship_results.meanSquaredError //0.4516
ship_results.meanAbsoluteError 

df.select(corr('crew','passengers')).show( )

