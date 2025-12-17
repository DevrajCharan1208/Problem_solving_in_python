# m = int(input("Elements in list 1 : "))

# l1 = [0 for m in range (m)]

# for i in range(m):
#     l1[i]= int(input(f"Enter your {i+1} element : "))
    
# n = int(input("Elements in list 2 : "))
# l2 = [0 for n in range (n)]
# for i in range(n):
#     l2[i]= int(input(f"Enter your {i+1} element : "))

l1 = [1,3,4,5,2,4]
l2 = [2,5,6,8,28,9]
# l1 = set(l1)
# l2 = set(l2)

# # print(l1)
# # print(l2)
# l3 = l1.intersection(l2)
# l4 = l1.union(l2)

# # print(l3,"\n",l4)
# print("Common elemnts of both lists : ", l1.intersection(l2))
# print()
# print()
# print("Unique elements of both lists : ", l3.symmetric_difference(l4))


l5 = []
l6 = []
for i in range(len(l1)):
    if l1.count([l1(i)]) > 1:
        l5.append(l1[i])
for i in range(len(l2)):
    if l2.count(l2[i]) > 1:
        l5.append(l2[i])
for i in range(len(l5)):
    if l5.count(l5[i]) > 1:
        l6.append(l5[i])
print (l6)