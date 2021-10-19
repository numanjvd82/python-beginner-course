# Getting input from the user

name = input("Enter Your Name: ")
if len(name) > 0:
    print("Hello " + name + "!")
    age = input("Enter Your Age in Numbers: ")
    if len(age) > 0 and int(age) > 0:
        if int(age) <= 14:
            print('You are a child right now')
        elif int(age) > 14 and int(age) < 18:
            print('You are a teenager right now')
        elif int(age) >= 18:
            print('You are an adult right now')
    else:
        print("Wrong Input")
else:
    print("You did not enter your name!")
