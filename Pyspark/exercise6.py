//mean of close column

from pyspark.sql.fucntions import mean
df.select(mean("Close")).show()
