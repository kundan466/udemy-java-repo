# recommended systems
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

spark=SparkSesssion.builder.appName('rec').getOrCreate()
data=spark.read.csv('movielens_rating.csv',header=True,inferSchema=True)
training,test=final_data.randomSplit([0.7,0.3])
als=ALS(maxIter=5,regParam=0.01,userCol='userId',itemCol='movieId',ratingCol='rating')
model=als.fit(training)
predictions=model.transform(test)
evaluator=RegressionEvaluator(metricName='rmse',labelCol='rating',
                             predictionCol='prediction')
rmse=evaluator.evaluate(predictions)  #1.884

single_user=test.filter(test['userId']==11).select(['movieId','userId'])
recommendations=model.transform(single_user)
recommendations.orderBy('prediction',ascending=False).show()

