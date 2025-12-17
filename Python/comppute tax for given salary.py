income = int(input("Enter your annual income "))

if income <= 500000:
    tax = 0
elif income <= 800000:
    tax = (income - 500000) * 5/100
elif income <= 1100000:
    tax = (300000 * 5/100) + (income - 800000) * 10/100
elif income <= 1400000:
    tax = (300000 * 5/100) + (300000 * 10/100) + (income - 1100000) * 15/100
elif income <= 1800000:
    tax = (300000 * 5/100) + (300000 * 10/100) + (300000 * 15/100) + (income - 1400000) * 20/100
elif income <= 2000000:
    tax = (300000 * 5/100) + (300000 * 10/100) + (300000 * 15/100) + (400000 * 20/100) + (income - 1800000) * 25/100
else:
    tax = (300000 * 5/100) + (300000 * 10/100) + (300000 * 15/100) + (400000 * 20/100) + (200000 * 25/100) + (income - 2000000) * 30/100

print("Total tax deduction =", tax)