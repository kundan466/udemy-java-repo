#logistic regression exercise

from pyspark.sql import SparkSession
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LogisticRegression

spark=SparkSesssion.builder.appName('logregconsult').getOrCreate()
df=spark.read.csv('customer_churn.csv',header=True,inferSchema=True)
assembler=VectorAssembler(inputCols=['Age',
                                    'Total_Purchase',
                                    'Account_Manager',
                                    'Years',
                                    'Num_Sites'],outputCol='features')
output=assembler.transform(data);
final_data=output.select('[features','churn'])
train_churn,test_churn=final_data.randomSplit([0.7,0.3])
lr_churn=LogisticRegression(labelCol='churn')
fitted_churn_model=lr_churn.fit(train_churn)
training_sum=fitted_churn_model.summary
pred_and_labels=fitted_churn_model.evaluate(test_churn)
churn_eval=BinaryClassificationEvaluator(rawPredictionCol='prediction',
                                        labelCol='churn')
auc=churn_eval.evaluate(pred_and_labels.predictions) //0.68


#predict on new data
final_lr_model=lr.churn.fit(final_data)
new_customers=spark.read.csv('new_customers.csv',header=True,inferSchema=True)
test_new_customers=assembler.transform(new_customers)
final_results=final_lr_model.transform(test_new_customers)
final_results.select('Company','predictions').show()
