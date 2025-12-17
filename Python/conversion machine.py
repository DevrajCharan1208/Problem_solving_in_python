# a = 1
# while (a!=4):
#     print ("1. Binary")
#     print ("2. octal")
#     print ('3. Hexadecimal')
#     print ("4. Exit")
#     a = int(input("Enter your choice"))
#     if (a==1):
#         print ("\nConverting to binary . . .\n")
#         x = int(input("Enter the decimal number : "))
#         i = 0
#         n = ""
#         while (a>0):
#             i  = a%2
#             a = a//2
#             n = str(i)+ n
#         print ('\n',n,"\n")
#     elif (a==2):
#         print ("\nConverting to octal . . .\n")
#         x = int(input("Enter the decimal number : "))
#         i = 0
#         n = ""
#         while (a>0):
#             i  = a%8
#             a = a//8
#             n = str(i)+ n
#         print ('\n',n,"\n")
#     elif (a==3):
#         print ("\nConverting to hexadecimal . . .\n")
#         x = int(input("Enter the decimal number : "))
#         hexadecimal = ""
#         hexa_char = [1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
#         while x > 0:
#             remainder = x % 16
#             hexadecimal = str(hexa_char[remainder-1]) + hexadecimal
#             x = x//16
#         print('\n',hexadecimal,"\n")
#     elif (a==4):
#         print ("Exit from program")
#     else:
#         print("Invalid choice...")
        
    
a = 1
while (a!=4):
    print ("1. Binary\n")
    print ("2. octal\n")
    print ('3. Hexadecimal\n')
    print ("4. Exit\n")
    a = int(input("Enter your choice : "))
    match a:
        case 1: 
            print ("\nConverting to binary . . .\n")
            x = int(input("Enter the decimal number : "))
            i = 0
            n = ""
            while (x>0):
                i  = x%2
                x = x//2
                n = str(i)+ n
            print ('\n',n,"\n")
        case 2:
            print ("\nConverting to octal . . .\n")
            x = int(input("Enter the decimal number : "))
            n = ""
            while (x>0):
                i  = x%8
                x = x//8
                n = str(i)+ n
            print ('\n',n,"\n")
        case 3:
            print ("\nConverting to hexadecimal . . .\n")
            x = int(input("Enter the decimal number : "))
            hexadecimal = ""
            hexa_char = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
            while x > 0:
                remainder = x % 16
                hexadecimal = str(hexa_char[remainder]) + hexadecimal
                x = x//16
            print('\n',hexadecimal,"\n")
        case 4:
            print ("\nExiting from the machine\n")
            print (("Thanks for using").center(20,'.'))
        case _:
            print("\ninvalid choice\n")