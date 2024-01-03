//avg close for each calender month

monthdf=df.withColumn('Month',month('Date'))
month_avgs=monthdf.select(['Month','Close']).groupBy('Month').mean()
month_avgs.select('Month','avg(Close)').orderBy('Month').show()
