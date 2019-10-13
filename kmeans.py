import sys
import random as r
import math
import matplotlib.pyplot as plt

def convergence(centroids,new_centroids,k):
    for i in range(k):
        d=math.sqrt( (centroids[i][0]-new_centroids[i][0])**2+(centroids[i][1]-new_centroids[i][1])**2 )
        if d>0.1:
            return False
    return True        

path=sys.argv[1]
k=int(sys.argv[2])

#read data from the file and create the python dataset
#vector features in l list
l=[]
f=open(path)
lines=f.readlines() #lines=["1,0\n",...]
for i in range(len(lines)):
    temp_str=lines[i]
    a=float(temp_str[0])
    b=float(temp_str[2])
    temp_list=[a,b]
    l.append(temp_list)

#plot the training data 
l_x=[]
l_y=[]
for i in range(len(l)):
    l_x.append(l[i][0])
    l_y.append(l[i][1])
plt.plot(l_x,l_y,'ro')
plt.show()

#k-means starts
#randomly select k-centroids
centroids=[]
for i in range(k):
    x=r.uniform(0,8)
    y=r.uniform(0,8)
    temp=[x,y]
    centroids.append(temp)

cluster=[]
new_centroids=[]
for i in range(len(l)):
    cluster.append(0)
for i in range(k):    
    new_centroids.append([0,0])   
    
while True:
    #assign each data point to the closest centroid
    for i in range(len(l)):
        min=50
        cl=0
        #for each data point compute the d(data point,centroid)
        for j in range(k):
            temp=math.sqrt( (centroids[j][0]-l[i][0])**2+(centroids[j][1]-l[i][1])**2 )        
            if temp<min:
                min=temp
                cl=j
        cluster[i]=cl
    #recompute centroids
    #for each cluster compute its new centroid    
    for i in range(k):
        sumX=0
        sumY=0
        cntr=0
        for j in range(len(l)):
            if cluster[j]==i:
                sumX+=l[j][0]
                sumY+=l[j][1]
                cntr+=1
        new_centroids[i][0]=float(sumX/cntr)
        new_centroids[i][1]=float(sumY/cntr)

    #the algorithm converges if the new centroids' distance from the old centroids is < 0.1
    if convergence(centroids,new_centroids,k):
        break

    centroids=new_centroids[:]

#print the data points and the cluster that they belong to
for i in range(len(l)):
    print (l[i],cluster[i])

f.close()    
