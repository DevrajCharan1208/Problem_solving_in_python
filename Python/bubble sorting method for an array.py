#Bubble sorting 
from array import *
array1 = array('i',[150,16,200,301,420,250,140])
for i in range(0,len(array1)-1):
    for j in range(0,len(array1)-1-i):
        if (array1[j]>array1[j+1]):
            t = array1[j]
            array1[j]= array1[j+1]
            array1[j+1]= t
for x in array1:
    print(x,end=" ")