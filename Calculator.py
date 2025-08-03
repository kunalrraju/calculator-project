def addition(num1: float, num2: float) -> float:
    return num1 + num2

def subtraction(num1: float, num2: float) -> float:
    return num1 - num2

def multiplication(num1: float, num2: float) -> float:
    return num1 * num2

def division(num1: float, num2: float) -> float:
    if num2 != 0:
        return num1 / num2
    else:
        return "Error : Division by 0"

def power(num1: float, num2: float) -> float:
    return num1**num2

def modulo(num1: float, num2: float) -> float:
    return num1%num2

def integer_division(num1: float, num2: float) -> float:
        return num1//num2
loop_exit=False
while loop_exit==False:

    num1 = float(input("Enter the first number please \n> "))
    num2 = float(input("Enter the second number please \n> "))
    operation = input("Choose operation please (+, -, *, /, **, %, //) : \n + : Addition\n - : Subtraction\n * : multiplication\n / : normal Division\n ** : Exponent\n % : modulo function\n // : Integer Division\n>"  )

    if operation=="+":
        print(addition(num1,num2))
    elif operation=="-":
        print(subtraction(num1,num2))
    elif operation=="*":
        print(multiplication(num1,num2))
    elif operation=="/":
        print(division(num1,num2))
    elif operation=="**":
        print(power(num1,num2))
    elif operation=="%":
        print(modulo(num1,num2))
    elif operation=="//":
        print(integer_division(num1,num2))

    else:
        print("invalid operation")
    continue_user_input=input("If you would like to continue using the calculator, click enter, else click anything?\n>")

    if continue_user_input!="":
        loop_exit=True




