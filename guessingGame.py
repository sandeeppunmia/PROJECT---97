import random
number = random.randint(0, 5)
print("Number Guessing Game")
guess = int(input("Guess a number between 1 - 9 :-"))
if(guess == number):
    print("Well Done!!! You have guessed the correct number")
else:
    print("Sorry, you have guessed the wrong number - 4 more chances left")
    chances = 0
    while(chances < 5):
        chances = chances + 1
        if(chances >= 5):
            print("You Lose!!! The correct number is ",number)
            break
        nextGuess = int(input("Try again"))
        if(nextGuess == number):
            print("Well Done!!! You have guessed the correct number")
            break