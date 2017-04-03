import urllib
import pandas as pd
import os
df = pd.read_csv('Shorts.csv')
k = df.imageUrlStr
l = len(df)

for i in range(25001,30000):
    if not pd.isnull(k[i]):
            images = k[i].split(';')
            urllib.urlretrieve(images[1],'image/'+str(i)+'.jpeg')

print "Done!"

