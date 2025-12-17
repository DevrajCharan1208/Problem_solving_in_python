# l1 = [12,"VIT",2.5,"bhopu",15,25,9]  # one-dimentional list

l2 = [[12,23,24],[10,11,16],[20,30,40]]  #two dimentional list, 
l3 = [[1,2,3],[4,5,6],[7,8,9]] #where every list inside the list is a row of matrix
l4 = []
A = []
B = []
C = []
# for i in range(len(l1)):
#     print(l1[i],end = " ") # one-dimentional list
    
    
# print()
# for i in range(len(l2[0])):
#     print(l2[i])
#     print()
    
    
# for i in range (len(l2[0])):
#     for j in range(len(l2[0])):
#         print(l2[i][j],end = " ")
#     print()


for i in range (len(l2[0])):
    for j in range(len(l2[0])):
        print(l2[i][j]+l3[i][j],end = " ")
    print()
    
    
for i in range (len(l2[0])):
        a = (l2[0][i]+l3[0][i])
        b = (l2[1][i]+l3[1][i])
        c = (l2[2][i]+l3[2][i])
        A.append(a)
        B.append(b)
        C.append(c)
l4 = [A,B,C]
for i in range (len(l4[0])):
    for j in range(len(l4[0])):
        print(l4[i][j],end = " ")
    print()
