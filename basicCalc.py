# Addition
def do_addition(num1, num2):
    return num1 + num2

# Show Calculator Options


def show_calc_options():
    option1 = input("Enter 1 to add two numbers:\n2 To Subtract Numbers ")

    if int(option1) == 1:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print(do_addition(int(num1), int(num2)))


show_calc_options()
