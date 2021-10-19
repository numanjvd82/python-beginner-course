# Addition
def do_addition(num1, num2):
    return num1 + num2

# Subtraction


def do_subtraction(num1, num2):
    return num1 - num2

# Show Calculator Options


def show_calc_options():
    option1 = input(
        "Enter 1 to add:\nEnter 2 To Subtract:\nEnter 3 to Divide:\nEnter 4 to Multiply:  ")

    if int(option1) == 1:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print(do_addition(int(num1), int(num2)))
    elif int(option1) == 2:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print(do_subtraction(int(num1), int(num2)))
    else:
        print("Invalid option")


show_calc_options()
