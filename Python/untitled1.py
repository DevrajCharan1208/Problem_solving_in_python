m = int(input("input number of rows: "))
n = int(input("input number of columns: "))

l = [[0 for n in range (n)] for m in range(m)]

for i in range(m):
    for j in range(n):
        l[i][j] = int(input())
        # print(l[i][j],end =" ")
    print()