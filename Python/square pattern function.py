
def squarepattern(s):
    for i in range (s):
        if (i == 0 or i == (s-1)):
            print("* "*s)
        else:
            print("*" + " "*(2*s-3) + "*")
squarepattern(5)