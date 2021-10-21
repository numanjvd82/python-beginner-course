# Guessing Game

secretWord = "Mr Robot"
guess = ""
limit = 4

while guess != secretWord:
    if limit == 0:
        print("You have no more guesses left!")
        break
    userResponse = input(
        "Guess the Word: Some Hints are (drama, netflix, hacker, conglomerate, economy): ")
    if userResponse == secretWord:
        print("You got it right!")
        break
    else:
        print("Wrong! Try again")
        limit -= 1
