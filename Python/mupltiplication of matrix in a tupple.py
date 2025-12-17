t1 = ((1,2,3),(3,4,5),(5,6,7))
t2 = ((1,2,3),(3,4,5),(5,6,7))
print("Multiplication of Two matrices : ")
for i  in range(3):
    for j in range(3):
        c = 0
        for k in range(3):
            c = c + t1[i][k]*t2[k][j]
        print(c,end = " ")
    print()

print()
print()
print()
print("Transpose of the matrix :")


for i  in range(len(t1[0])):
    for j in range(len(t1[0])):
        trans_element = t1[j][i]
        print(trans_element,end=" ")
    print()