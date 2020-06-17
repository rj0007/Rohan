# exercise6 Snake water gun game

import random

list = ['s', 'w', 'g']
noOfChancesYouHave = 10
computerPoints = 0
yourPoints = 0
tie = 0
print("Snake Water Gun Game and You have " + str(noOfChancesYouHave) + " chances in this Game")

while noOfChancesYouHave > 0:

    _input = input("s for snake / g for Gun / w for Water : ")
    _random = random.choice(list)

    if _input == _random:
        tie += 1
        print("You entered " + _input + " and computer guesses " + _random)
        print("Tie and 0 points to each and you have only " + str(noOfChancesYouHave - 1) + " left")

    elif _input == "s" and _random == "g":
        computerPoints += 1
        print("You entered " + _input + " and computer guesses " + _random)
        print("Computer win 1 point and you have only " + str(noOfChancesYouHave - 1) + " left")

    elif _input == "s" and _random == "w":
        yourPoints += 1
        print("You entered " + _input + " and computer guesses " + _random)
        print("You win 1 point and you have only " + str(noOfChancesYouHave - 1) + " left")

    elif _input == "w" and _random == "g":
        yourPoints += 1
        print("You entered " + _input + " and computer guesses " + _random)
        print("You win 1 point and you have only " + str(noOfChancesYouHave - 1) + " left")

    elif _input == "w" and _random == "s":
        computerPoints += 1
        print("You entered " + _input + " and computer guesses " + _random)
        print("Computer win 1 point and you have only " + str(noOfChancesYouHave - 1) + " left")

    elif _input == "g" and _random == "w":
        computerPoints += 1
        print("You entered " + _input + " and computer guesses " + _random)
        print("Computer win 1 point and you have only " + str(noOfChancesYouHave - 1) + " left")

    elif _input == "g" and _random == "s":
        yourPoints += 1
        print("You entered " + _input + " and computer guesses " + _random)
        print("You win 1 point and you have only " + str(noOfChancesYouHave - 1) + " left")

    else:
        print("You enter a wrong input")

    noOfChancesYouHave -= 1

print("Game Over")

if computerPoints > yourPoints:
    print("Computer Wins by " + str(computerPoints - yourPoints) + " points")
if yourPoints > computerPoints:
    print("You won by " + str(yourPoints - computerPoints) + " point/s")
print(
    "Your total points are " + str(yourPoints) + " and computer total points are " + str(computerPoints) + "Tie " + str(
        tie) + " times")