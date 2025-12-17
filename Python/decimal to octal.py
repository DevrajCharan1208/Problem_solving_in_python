a = int(input("enter the decimal number :"))

binary = ""
while (a>0):
    remainder = a%2
    a = a//2
    binary = str(remainder)+ binary
print (binary)


octal = ""
while a > 0:
    remainder = a % 8
    octal = str(remainder) + octal
    a = a // 8

print(octal)


hexadecimal = ""
hexa_char = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
while a > 0:
    remainder = a % 16
    hexadecimal = str(hexa_char[remainder]) + hexadecimal
    a = a//16
print(hexadecimal)
    
