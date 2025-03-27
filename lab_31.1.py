import csv
list_cat=[]
list_name=[]
list_desc=[]
list_avail=[]

filename=input()

with open(filename,'r') as csvfile:
    foodlist=csv.reader(csvfile,delimiter='\t')
    for row in foodlist:
        list_cat.append(row[0])
        list_name.append(row[1])
        list_desc.append(row[2])
        list_avail.append(row[3])

for line in range(len(list_avail)):
    if list_avail[int(line)]=='Available':
        print(f'{list_name[line]} ({list_cat[line]}) -- {list_desc[line]}')
