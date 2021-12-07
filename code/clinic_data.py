import json
import os
import csv
import pandas as pd

json_file = 'clinical.cart.2021-02-04.json'
meta_file = 'metadata.cart.2021-02-04.json'


f = open(json_file)
json_data = json.load(f)


cases = {}


i = 0
for clinic in json_data:
    i+= 1
    try:
        diagnoses = clinic['diagnoses']
    except:
        continue
    for item in diagnoses:
        primary = item["primary_diagnosis"]
        tissue = item["tissue_or_organ_of_origin"] 
    case_id = clinic['case_id']
    #print(i ,case_id, primary)
    cases[case_id] = [primary, tissue]

f.close()

print(len(cases))

f = open(meta_file)
meta_json_data = json.load(f)


for data in meta_json_data:
    file_name = data["file_name"]
    for m in data["associated_entities"]:
        c = m['case_id']
    try:
        cases[c].append(file_name)
    except:
        continue

for key,item in cases.items():
    item[0],item[2] = item[2], item[0]
    cases[key] = item
    
to_csv=[]
for key,item in cases.items():
    empty =[key, item[0],item[1], item[2]]
    to_csv.append(empty)
#print(to_csv)    
#print(cases)
f.close()
columns= ['Case_ID', 'File_name', 'Tissue','Primary Diagnosis', ]

df = pd.DataFrame(to_csv)
df.to_csv('labels.csv', index=False, header=columns)

