n = 5
while (n>0):
    for i in range(n):
        print(n,end = " ")
    print()
    n = n -1
    
    
print()
print()
    
a = 6
c = a
b = "  *  "
while(a>0):
    print(f"{b*a}".center(len(b)*c))
    a = a-1
    