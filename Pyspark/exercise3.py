from pyspark.sql.functions import format_number
result=df.describe()
result.select(result['summary'],
             format_number(result['Open'].cast('float'),2).alias('Open'),
             format_number(result['High'].cast('float'),2).alias('High')
             format_number(result['Low'].cast('float'),2).alias('Low')
             format_number(result['Close'].cast('float'),2).alias('Close')
             result['Volume'].cast('int').alias('Volume')).show()
