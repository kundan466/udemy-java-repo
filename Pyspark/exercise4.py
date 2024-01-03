//HVratio

df2=df.withColumn("HV Ratio",df['High']/df['Volume'])
df2.select('HV Ratio').show()
