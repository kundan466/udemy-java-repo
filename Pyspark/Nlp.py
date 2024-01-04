# nlp

from pyspark.sql import SparkSession
from pyspark.sql.functions import length
from pyspark.ml.features import Tokenizer,StopWordsRemover,CountVectorizer,IDF,StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import NaiveBayes
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark=SparkSesssion.builder.appName('nlp').getOrCreate()
data=spark.read.csv('smsspamcollection/SMSSpamCollection',inferSchema=True,sep='\t')
data=data.withColumnRenamed('_c0','class').withColumnRenamed(_'c1','text')
data=data.withColumn('length',length(data['text']))
data.groupBy('class').mean().show()  #feature engineer
tokenizer=Tokenizer(inputCol='text',outputCol='token_text')
stop_remove=StopWordsRemover(inputCol='token_text',outputCol='stop_token')
count_vec=CountVectorizer(inputCol='stop_token',outputCol='c_vec')
idf=IDF(inputCol='c_vec',outputCol='tf_idf')
ham_spam_to_numeric=StringIndexer(inputCol='class',outputCol='label')
clean_up=VectorAssembler(inputCols=['tf_idf','length'],outputCol='features')
nb=NaiveBayes()
data_prep_pipe=Pipeline(stages=[ham_spam_to_numeric,tokenizer,stop_remove,
                               count_vec,idf,clean_up])
leaner=data_prep_pipe.fit(data)
clean_data=cleaner.transform()
clean_data=clean_data.select('label','features')
training,test=clean_data.randomSplit([0.7,0.3])
spam_detector=nb.fir(training)
test_results=spam_detector.transform(test)
acc_val=MulticlassClassificationEvaluator()
acc=acc_eval.evaluate(test_results)
