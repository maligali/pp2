import random

name = input("Hello! What is your name?\n")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
answ = random.randrange(1, 21)

def game(answ, guessnum):
    num = int(input("Take a guess.\n"))
    if answ == num:
        print(f"Good job, {name}! You guessed my number in {guessnum} guesses!")
    elif num < answ:
        print("Your guess is too low")
        game(answ, guessnum + 1)
    else:
        print("Your guess is too high")
        game(answ, guessnum + 1)

game(answ, 0)