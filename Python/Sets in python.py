s2 = {1,2,4,5,6}
print("{", end = " ")
for i in range(len(s2)):
    print(s2.pop(),end = "")
print("}")

    
    
s1 = {2,3,1}
s2 = {6,8,10,10}
s3 = {4,5,6}
s2.symmetric_difference_update(s3)
print(s2)

