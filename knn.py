import sys
import random as r
import math
import matplotlib.pyplot as plt

def bubbleSort(arr,label):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                label[j],label[j+1]=label[j+1],label[j]
    
path=sys.argv[1]
k=int(sys.argv[2])

#read data from the file and create the python dataset
#features in l list and label in label list
l=[]
label=[]
f=open(path)
lines=f.readlines() #lines=["1,0,0\n",...]
for i in range(len(lines)):
    temp_str=lines[i]
    a=float(temp_str[0])
    b=float(temp_str[2])
    c=int(temp_str[4])
    temp_list=[a,b]
    l.append(temp_list)
    label.append(c)
    
#generate an input to classify it
x=r.uniform(0,3)
y=r.uniform(0,3)

#plot the training data 
l_x=[]
l_y=[]
colors=[]
for i in range(len(l)):
    l_x.append(l[i][0])
    l_y.append(l[i][1])
plt.plot(l_x,l_y,'ro')
plt.show()

#compute distance matrix d
#euclidean distance
d=[]
for i in range(len(l)):
    temp_d=math.sqrt( (x-l[i][0])**2+(y-l[i][1])**2 )        
    d.append(temp_d)
    
#bubblesort d ASCENDING and swaps at the label matrix
bubbleSort(d,label)

#knn and majority vote
cntr0,cntr1=0,0
for i in range(k):
    if label[i]==0:
        cntr0+=1
    else:
        cntr1+=1
if cntr0>cntr1:
    print("the input is labeled as 0")
else:
    print("the input is labeled as 1")

f.close()
