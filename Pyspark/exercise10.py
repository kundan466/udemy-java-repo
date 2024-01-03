//pearson correlation between high and volume

df.select(corr('High','Volume')).show()
