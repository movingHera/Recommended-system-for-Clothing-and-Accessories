import pandas as pd
import csv
ct = 0
df  = pd.read_csv('2oq-c1r.csv')
k =  df.categories
l = len(k)
with open('Shorts','wb') as f:
    writer = csv.writer(f,delimiter=',')
    writer.writerow(df.columns.values)
    for i in range(1,l):
        if not pd.isnull(k[i]):
            r =k[i].split('>')
            if 'Shorts' in r:
                ct+=1
                writer.writerow(df.iloc[i])

print ct
