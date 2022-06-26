import csv
from dataclasses import dataclass

dataset1=[]
with open("stars.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
 
dataset2=[]
with open("dwarfstars.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

header1=dataset1[0]
header2=dataset2[0]
dataset1rows=dataset1[1: ]
headers=header1+header2
dataset2rows=dataset2[1: ]

stars_data=[]
for index,data_row in enumerate(dataset1rows):
    stars_data.append(dataset1rows[index]+dataset2rows[index])
with open("allstars.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)   


    

