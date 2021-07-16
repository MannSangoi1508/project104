import csv
from collections import Counter

def mean():
with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(float(n_num))



n = len(new_data)
total =0
for x in new_data:
    total += x

mean = total / n

print("Mean / Average is: " + str(mean))

def median():
with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)

n = len(new_data)
new_data.sort()


if n % 2 == 0:
    
	median1 = float(new_data[n//2])
   
	median2 = float(new_data[n//2 - 1])
    
	median = (median1 + median2)/2
else:
	median = new_data[n//2]

print("Median is: " + str(median))

def mode():
with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)


n = len(new_data)

data = Counter(new_data)

get_mode = dict(data)

mode = []
mode1 = []
mode2 = []


for a,v in get_mode.items():
    
    a= float(a)
    if 50< a <60:
       
        if v == max(list(data.values())):
            mode.append(a)
    elif 60< a <70:
        if v == max(list(data.values())):
            mode1.append(a)
    elif 70< a <75:
        if v == max(list(data.values())):
            mode2.append(a)



if len(mode)>len(mode1) and len(mode2):
    print("Mode is /are "+ ', '.join(map(str, mode)))
elif len(mode1)>len(mode) and len(mode2):
    print("Mode is /are "+ ', '.join(map(str, mode1)))
elif len(mode2)>len(mode) and len(mode1):
    print("Mode is /are "+ ', '.join(map(str, mode2)))
