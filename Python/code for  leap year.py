Year = int(input("Enter the year : "))
print()
print(Year)
if (Year%4 == 0) :
    if (Year % 100 == 0 and Year % 400 != 0):
        print(f"{Year} is not a leap year")
    else:
        print(f"{Year} is a leap year")
   
else: 
    print(f"{Year} is not a leap year")


# Year = int(input("Enter the year : "))
# print()
# print(Year)
# if (Year%4 == 0 and Year%100!= 0) or (Year%400 ==0) :
  
#         print(f"{Year} is a leap year")
   
# else: 
#     print(f"{Year} is not a leap year")