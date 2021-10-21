# Try Except is just like try catch in javaScript


try:
    number = int(input("Enter a number: "))
    if int(number):
        print(number)
except ValueError as err:
    print(err)
