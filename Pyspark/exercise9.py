//time is high than 80

(df.filter(df['High']>80).count()*1.0/df.count())*100
