//max high per year

yeardf=df.withColumn("Year",year(df['date']))
max_df=yeardf.groupBy('Year').max()
max_df.select('Year','max(High)').show()
