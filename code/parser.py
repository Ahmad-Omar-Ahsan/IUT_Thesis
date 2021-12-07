import pandas as pd 
df = pd.read_csv('labels.csv')
labels = {}

for i in df['Primary Diagnosis']:
    labels[i] = labels.get(i, 0) + 1

sort_orders = sorted(labels.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
	print(i[0], i[1])
