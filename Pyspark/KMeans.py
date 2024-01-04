#k means clustering

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler,StandardScalar
from pyspark.ml.clustering import KMeans

spark=SparkSesssion.builder.appName('cluster').getOrCreate()
data=spark.read.csv('nack_data.csv',header=True,inferSchema=True)
feat_cols=['Session_Connection_Time',
          'Byte_Transferred',
          'Kali_Trace_Used',
          'Servers_Corrupted',
          'Pages_Corrupted',
          'WPM_Typing_Speed']

assembler=VectorAssembler(inputCols=feat_cols,outputCol='features')
final_data=assembler.transform(dataset)
scaler=StandardScalar(inputCol='features',outputCol='scaledFeatures')
scaler_model=scaler.fit(final_data)
cluster_final_data=scaler_model.transform(final_data)
kmeans2=KMeans(featuresCol='scaledFeatures',k=2)
kmeans3=KMeans(featuresCol='scaledFeatures',k=3)
model_k2=kmeans2.fit(cluster_final_data)
model_k3=kmeans3.fit(cluster_final_data)

# model_k3.transform(cluster_final_data).groupBy('prediction').count().show()
# model_k2.transform(cluster_final_data).groupBy('prediction').count().show()
