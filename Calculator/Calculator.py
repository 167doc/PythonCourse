from decimal import Decimal


print("Welcome to the Calculator")
print("Enter first number")
a=Decimal(input()) #e.g.:pi 3.14
print("Enter second number")
b=Decimal(input()) #e.g.: e 2.72


sum=round(a+b,2)
difference=round(a-b,2)
product=round(a*b,2)


print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")

if b!=0:
    quotient=round(a/b,2)
    print(f"Quotient:{quotient}")
else:
    print("Equals: Can't divide by zero")



print("Thank you for using Calculator")


