def calculate (num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return  num1 / num2
    else:
        print("Invalid operator!")

def calculator ():
        num1 = float(input("Enter a number: "))
        operator = input("Enter an operator: ")
        num2 = float(input("Enter a number: "))
        print("Result: " + str(calculate(num1, num2, operator)))
        decision = float(input("Press 1 to continue or 0 to exit: "))
        if decision == 1:
            calculator()
        else:
            exit()


calculator()
