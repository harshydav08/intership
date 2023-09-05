#Calculator
a = int(input("Enter first number: \n"))
b = int(input("Enter Second number: \n"))
c = str(input("Enter the operation!: \n"))
def calc(a,b,c):
    if c=="+":
        return a+b
    elif c=="-":
        return a-b
    elif c=="*":
        return a*b
    elif c=="/":    
        try:
            return a/b
        except:
            print("0 can not be divided by 0")
    elif c=="//":
        return a//b
    elif c=="%":
        return a%b
    else:
        return "Invalid input !!"

print(calc(a,b,c))