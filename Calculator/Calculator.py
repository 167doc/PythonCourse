

print("Welcome to the Calculator")
goon="y" #go on = yes
while (goon=="y"):
    print("Enter first number")
    a=float(input()) #e.g.:pi 3.14
    print("Enter second number")
    b=float(input()) #e.g.: e 2.72

    print("Choose operation: +, -, *, /")
    print("1 for addition")
    print("2 for substraction")
    print("3 for multiplication")
    print("4 for division")
    oper=int(input())


    #if, elif, else variant
    """if oper==1: resultoper=a+b
    elif oper==2: resultoper=a-b
    elif oper==3: resultoper=a*b
    elif oper==4:
        if b!=0: resultoper=a/b
        else:
            print("Can't divide by 0")
            resultoper="N/A"
    else: print("Impossible operation")
    
    if oper>0 and oper<5: print(f"Result: {resultoper}")
    else: print("Try again.")"""


    #match-case variant
    match oper:
        case 1:
            resultoper=a+b
            print(resultoper)
        case 2:
            resultoper=a-b
            print(resultoper)
        case 3:
            resultoper=a*b
            print(resultoper)
        case 4:
            if b==0:
                print("Can't divide by 0")
            else:
                resultoper = a / b
                print(resultoper)
        case _:
            print("Impossible operation")

    goon=input("Do you wish to try again? [y/n]: ").strip().lower()
print("Thank you for using Calculator")


