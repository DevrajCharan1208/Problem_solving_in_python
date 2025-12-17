# from array import *
# def bsearch(array1,n,low,high):
#     while(high>low):
#         print(high)
#         print(low)
#         mid = (low+high)//2
#         if(array1[mid]==n):
#             print ("number found",mid)
#             break
#         elif(array1[mid]<n):
#             low = mid +1
#         elif(array1[mid]>n):
#             high = mid-1
#     else:
#         print("number does not exist in array")
        
# array1 = array('i',[10,16,20,30,40,50,140])
# n = int(input("enter a number :"))
# low = 0 
# high = len(array1)-1
# bsearch(array1,n,low,high)



from array import *
def bsearch(array1,n,low,high):
    if(high>=low):
        print(high)
        print(low)
        mid = (low+high)//2
        if(array1[mid]==n):
            print ("number found",mid)
            
        elif(array1[mid]<n):
            bsearch(array1,n,mid+1,high)
        elif(array1[mid]>n):
            bsearch(array1,n,low,mid-1 )
    else:
        print("number does not exist in array")
        
array1 = array('i',[10,16,20,30,40,50,140])
n = int(input("enter a number :"))
low = 0 
high = len(array1)-1
bsearch(array1,n,low,high)
