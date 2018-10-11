#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:35:06 2018

@author: sumavenugopal
"""

#!/usr/bin/python

#https://www.yelp.com/dataset/download
import sys
import json
import csv
from datascience import *


ifilename = 'yelp_academic_dataset_review.json'

ofilename = 'yelp_academic_dataset_review.csv'

# LOAD DATA
json_lines = [json.loads( l.strip() ) for l in open(ifilename).readlines() ]
OUT_FILE = open(ofilename, "w")
root = csv.writer(OUT_FILE)
root.writerow(["business_id","text"])
json_no = 0 
for l in json_lines:
 root.writerow([l["business_id"], l["text"]])
 
 json_no += 1

print('Finished {0} lines'.format(json_no)) 
OUT_FILE.close()    




csv_file = 'yelp_academic_dataset_review.csv'
txt_file = 'yelp_academic_dataset_review.txt'



with open(txt_file, "w") as out_file:
    with open(csv_file, "r") as in_file:
        [ out_file.write("StartofReview".join(row)+'EndofReview\n') for row in csv.reader(in_file)]
    out_file.close()
 

    
    
