# Guess number game
no = 18
print("Welcome To The Guessing Game")
print("You only have 9 guesses")
noOfGuess = 1
while noOfGuess <= 9:
    guess = int(input("Guess The Number: "))
    if guess > no:
        print("The number is Bigger")
    elif guess < no:
        print("The number is Smaller")
    else:
        print("Congratulations You Won\n", "You took", noOfGuess, "Guesses")
        break
    print("You have", 9 - noOfGuess, "Guesses left")
    noOfGuess += 1
if noOfGuess > 9:
    print("Game Over")
