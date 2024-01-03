from pyspark.sql.functions import format_number
result=df.describe()
result.select(result['summary'],
             format_nuber(result['Open'].cast('float'),2).alias('Open'),
             format_nuber(result['High'].cast('float'),2).alias('High')
             format_nuber(result['Low'].cast('float'),2).alias('Low')
             format_nuber(result['Close'].cast('float'),2).alias('Close')
             result['Volume'].cast('int').alias('Volume')).show()
