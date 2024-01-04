#random forest
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier


spark=SparkSesssion.builder.appName('tree_consult').getOrCreate()
data=spark.read.csv('dog_food.csv',header=True,inferSchema=True)
assembler=VectorAssembler(inputCols=['A','B','C','D'],outputCol='features')
output=assembler.transform(data)
rfc=RandomForestClassifier(labelCol='Spoiled',featuresCol='features')
final_data=output.select(['features','Spoiled'])
rfc_model=rfc.fit(final_data)
# rfc_model.featureImportances
