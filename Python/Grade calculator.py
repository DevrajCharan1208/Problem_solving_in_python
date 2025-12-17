phy = int(input("marks of physics"))
chy = int(input("marks of chemistry"))
math = int(input("marks of maths"))

n = (phy+chy+math)/3
print("average marks=", n)

if (n>40):
    if (n<=50):
        print("E- grade")
    elif (n<=60):
        print("D- grade")
    elif(n<=70):
        print("C-grade")
    elif(n<=80):
        print("B-grade")
    elif(n<=90):
        print("A-grade")
    else: 
        print("S-grade")
else:
    print("fail")
    


        
    
    
