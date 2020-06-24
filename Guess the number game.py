# guess the number Game
import random

n = random.randint(1,101)
guesses = 9
i=1
print("Guess the number between 1 and 100")
while(i<=guesses):
    m = int(input("Enter number to guess: "))
    if m>n:
        print("Enter small number and only ", guesses-i, "guesses left")
    elif m == n:
        print("Congo!! You guess the correct number")
        #break
    else:
        print("Enter a big number and only", guesses-i, "guesses left")
    guesses = guesses - 1
    if(guesses == 0):
        print("Defeat")