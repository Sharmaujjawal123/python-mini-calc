first = input("enter first number? ")
operator = input("enter operator(+,-,*,%,/): ")
second = input("enter second number? ")
first = eval(first)
second = eval(second)
if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first/second)
elif operator == '%':
    print(first%second)
else:
    print("invalid operation")




