# This is my first Python Project in some time
print("Welcome to the Simple Python Calculator\nYou will be asked to enter in two numbers\nThen you will be asked to pick an operation")
num1 = int(input("What is your first number?   ")) # Create the first number
num2 = int(input("What is your second number?   ")) # Create the second number
op = input("What is your operation? Please pick from * (Times) + (Adding)\n/(Division) or -(Subtraction)   ") # Create the operation
if op == "*": # For Multiplication
    sol = num1*num2
    print(sol)
if op == "+": # For Addition
    sol = num1+num2
    print(sol)
if op == "-" or op == "/": # Checking User Input
    usrCom = input("Currently, the calculator is set to Input1 - Input 2 or Input1/Input2\n Is this correct? y or n   ")
    if usrCom == "y" or usrCom == "Y" and op == "-": # User Correct run Sub
        sol = num1-num2
        print(sol)
    elif usrCom == "y" or usrCom == "Y" and op == "/": # User Correct run Div
        sol = num1/num2
        print(sol)
    elif usrCom == "n" or usrCom == "N" and op == "-": # User Incorrect run Sub
        sol = num2-num1
        print(sol)
    elif usrCom == "n" or usrCom == "N" and op == "/": # User Incorrect run Div
        sol = num2/num1
        print(sol)