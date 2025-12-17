from array import *
array1 = array('i', [10,40,20,30,40,50,40])
for x in array1:
    while array1.count(x) > 1:
        array1.remove(x)
        
for y in array1:
    print(y)