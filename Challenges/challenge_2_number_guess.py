"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 4 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():

    number = random.randint(1, 20)
    #print(number) # just for debugging purpose :-)
    print("I'm thinking of a number between 1 and 20")

    guess = int(input("Guess a number: "))

    for i in range(4) :
        #print(i) # just for debug
        if guess == number:
            print("You nailed it! Good job!")
            print("The answer is {}".format(number))
            break
        #give hint
        elif guess < number and i < 3:
            print("You are to low")
            print('You have {} guesses left'.format(3 - i))
            guess = int(input("Take another guess: "))
        elif guess > number and i < 3:
            print("You are to high")
            print('You have {} guesses left'.format(3 - i))  #could be more DRY as the to lines are repeated
            guess = int(input("Take another guess: "))
        elif i == 3:
        #tell user that it's over
        print("You lost. The answer is {}".format(number))

run_game()
