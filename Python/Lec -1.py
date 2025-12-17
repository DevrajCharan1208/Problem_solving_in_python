# fucntion without argument and no return value
def areac(): #defination of the function
    r = int(input("enter value of radius"))
    a= 3.14*r*r
    print("Area =", a)
areac() #calling of the function


# fucntion without argument and with return value
def areac(): #defination of the function
    r = int(input("enter value of radius"))
    a= 3.14*r*r
    return a
result = areac() #calling of the function
print(result)


#function with argument and return value
def areac(n): #defination of the function
   a= 3.14*n*n
   return a
    
r = int(input("enter value of radius"))
    
result = areac(r) #calling of the function
print(result)



#function with argument and return no value
def areac(n,s): #defination of the function
   a= 3.14*n*n
   print(a)
   print(s)
   
r = int(input("enter value of radius"))   
result = areac(r,"VIT Bhopal") #calling of the function

