a = int(input("Enter your number : "))
n = a-1
c = set()
while n>0 :
    if a % n == 0:
        c.add(n)
    n = n-1
A = sum(c)
if A==a :
    print (f"{a} is a perfect number")
else:
    print (f"{a} is not a perfect number")
