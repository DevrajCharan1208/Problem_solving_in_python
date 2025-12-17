t = ((10,2,52),(29,56,29),(30,40,50))
print(t)

for i in range(len(t[0])):
    for j in range (len(t[0])):
           print(t[i][j], end = " ")    
    print()
print()
print()          
print("slicing")           
#slicing = tuple[start:stop:Step]
# if stop is greater than last index it will print till the last index
print(t[0:100])
a = sorted(t)# give the sorted tuple in a list
b = any(t)#return true if any value is non-zero it will return true
c = all(t)#return true if all values are non-zero
print(a)
print(b)
print(c)

