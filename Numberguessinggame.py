import random

chances = 5
number=random.randint(1,9)

print("Number guessing game!")
while chances>0:

    guess=input("Guess a number between 1-9 ")
    if number < guess:
        print("Your number is too high try lower than that!")
    elif guess == number:
        print("Congrats You did it! :D You guessed the number!")
    else:
        print("You number is too low try higher than that!")
    chances=chances-1
    
if chances <= 0:
    print("You lose :( , the number is ",number)
