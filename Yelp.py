#!/usr/bin/python 

#https://www.yelp.com/dataset/download
import sys
import json
import csv


ifilename = sys.argv[1]
try:
 ofilename = sys.argv[2]
except:
 ofilename = ifilename + ".csv"

# LOAD DATA
json_lines = [json.loads( l.strip() ) for l in open(ifilename).readlines() ]
OUT_FILE = open(ofilename, "w")
root = csv.writer(OUT_FILE)
root.writerow(["business_id","name","address","hours","is_open","categories","city","state","postal_code","review_count","stars"])
json_no = 0 
for l in json_lines:
 root.writerow([l["business_id"], l["name"],l["address"],l["hours"],l["is_open"],l["categories"],l["city"],l["state"],l["postal_code"],l["review_count"],l["stars"]])
 json_no += 1

print('Finished {0} lines'.format(json_no)) 
OUT_FILE.close()    




csv_file = 'yelp_academic_dataset_business.json.csv'
txt_file = 'yelp_academic_dataset_business.txt'



with open(txt_file, "w") as out_file:
    with open(csv_file, "r") as in_file:
        [ out_file.write(" ".join(row)+'|||') for row in csv.reader(in_file)]
    out_file.close()
