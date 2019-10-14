import random

print("Let's play Rock Paper Scissors \n"
            +"Rock = 1 \n"
            +"Paper = 2\n"
            +"Scissor = 3")
player_score = 0
computer_score = 0
x = 0
while x < 3:

    while True:
        try:
            player_input = int(input('Please enter a number from 1 to 3: '))
            if player_input not in (1, 2, 3):
                raise ValueError
            else:
                break
        except ValueError:
                print("That is not a number from 1-3.  Please enter a number from 1-3")

    if player_input == 1:
            print("Your choice is Rock")
    elif player_input == 2:
            print("Your choice is Paper")
    elif player_input == 3:
            print("Your choice is Scissors")


    computer_input = random.randint(1, 3)
    if computer_input == 1:
        print("The computer's choice is Rock")
    elif computer_input == 2:
        print("The computer's choice is Paper")
    elif computer_input == 3:
        print("The computer's choice is Scissors")


    if (player_input == 1 and computer_input == 1):
        print("It's a tie.")
    elif (player_input == 2 and computer_input == 2):
        print("It's a tie.")
    elif (player_input == 3 and computer_input == 3):
        print("It's a tie.")
    elif (player_input == 1 and computer_input == 2):
        print("The computer won!")
        computer_score += 1

    elif (player_input == 1 and computer_input == 3):
        print("You won!")
        player_score += 1

    elif (player_input == 2 and computer_input == 1):
        print("You won!")
        player_score += 1

    elif (player_input == 2 and computer_input == 3):
        print("The computer won!")
        computer_score += 1

    elif (player_input == 3 and computer_input == 1):
        print("The computer won!")
        computer_score += 1

    elif (player_input == 3 and computer_input == 2):
        print("You won!")
        player_score += 1


    x = x + 1
print("Your score is: ", player_score)
print("The computer's score is: ", computer_score)
if player_score > computer_score:
    print("You beat the computer!  Good job!")
elif player_score < computer_score:
    print("The computer won!  Better luck next time.")
else:
    print("It's a tie!")
