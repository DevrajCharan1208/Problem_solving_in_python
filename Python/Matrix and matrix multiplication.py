# m = int(input("input number of rows for 1st matrix: "))
# n = int(input("input number of columns for 1st matrix: "))

# a = [[0 for col in range (n)] for row in range(m)]




# for i in range(m):
#     for j in range(n):
#         a[i][j] = int(input())
#         # print(l[i][j],end =" ")
#     print()
    
# for i in range(m):
#     for j in range(n):
#         print(a[i][j],end =" ")
#     print()
    
    
    
# p = int(input("input number of rows for 2nd matrix : "))
# q = int(input("input number of columns for 2nd matrix : "))

# b= [[0 for col in range (q)] for row in range(p)]

# for i in range(p):
#     for j in range(q):
#         b[i][j] = int(input())
#         # print(l[i][j],end =" ")
#     print()
    
# for i in range(p):
#     for j in range(q):
#         print(b[i][j],end =" ")
#     print()
  
# if (n ==p):
#     c = [[0 for col in range (q)] for row in range(m)]
#     for i in range(m):
#         for j in range(q):
#             for k in range(q):
#                 c[i][j] = c[i][j] + a[i][j]*b[k][j]
# else : 
#     print("Multipllication not possible")
                
# for i in range(m):
#      for j in range(q):
#          print(c[i][j],end =" ")
#      print() 
    
  
    
  
    
  
    
  
    
  
    
  
    
# # l3 = []   
# # A = []
# # B = []
# # C = []
# # f = 0
# # g = 0
# # h = 0
# # if (n ==p):
# #     for i in range (len(l2[0])):
# #             a = (l1[0][i]*l2[i][0])
# #             b = (l1[1][i]*l2[i][1])
# #             c = (l1[2][i]*l2[i][2])
            
# #             A.append(a)
# #             B.append(b)
# #             C.append(c)
# #     l3 = [A,B,C]




m=int(input("Enter number of rows for 1st matrix:"))
n=int(input("Enter number of columns for 1st matrix:"))
a=[[0 for n in range(n)] for m in range(m)]

for i in range(m):
    for j in range(n):
        #print(a[i][j],end=" ")
        a[i][j]=int(input())
        
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ") 
    print()
    
    
p=int(input("Enter number of rows for 2nd matrix:")) 
q=int(input("Enter number of columns for 2nd matrix:"))
b=[[0 for q in range(q)] for p in range(p)]

for i in range(p):
    for j in range(q):
        #print(a[i][j],end=" ")
        b[i][j]=int(input())
    print()
for i in range(p):
    for j in range(q):
        print(b[i][j],end=" ")
    print()

if(n==p):
    c=[[0 for q in range(q)] for m in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j]=c[i][j]+a[i][k]*b[k][j]
    for i in range(m):
        for j in range(q):
            print(c[i][j],end=" ")
        print()
                
else:
    print("Multiplication is not possible")







