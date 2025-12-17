n = int(input("nth term :"))
a = 1
b = 1

for i in range(n-2):
    x = a + b
    a = b
    b = x
    n = x
   

print (n)

