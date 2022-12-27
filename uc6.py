# uc6-----Report the number of times the dice was played to win the game and also the position after every die role
# -----------------------------------------------------------------------------------------------------------------
# uc3  --- option checking
import random


# Define a function to roll the die and return the result
def rollDie():
    roll = random.randint(1, 6)
    return roll


# Define a function to generate a random option (No Play, Ladder, or Snake) and return the result
def generateOption():
    option = random.randint(1, 3)
    if option == 1:
        return "No Play"
    elif option == 2:
        return "Ladder"
    else:
        return "Snake"


print("WELCOME TO SNAKE LADDER GAME")

player_position = 0
num_rolls = 0  # for uc6 count the rolls
#  game loop
while True:
    # Roll the die and generate an option
    die_roll = rollDie()
    option = generateOption()

    # Update the player's position
    if option == "No Play":
        player_position = player_position
    elif option == "Ladder":
        player_position += die_roll
    else:
        player_position -= die_roll
        # uc4 reset player position
        if player_position<0:
            player_position=0
            # uc5--player position stays at same position when dieroll >100
        elif player_position > 100:
            player_position = player_position - die_roll


    # Print the result of the player's turn
    print(f"You rolled a {die_roll} and got a {option}, your new position is {player_position}")
    # uc-6 --count total rolls
    num_rolls +=1

    # uc5-- winning at exact 100
    if player_position==100:
        print("CONGRATULATION! You won the game")
        # uc6 print statement
        print(f"It took you {num_rolls} rolls to win.")
        break

    # Ask the player if they want to continue playing
    choice = input("Do you want to continue playing? (Y/N) ")
    if choice.lower() != "y":
        break

print("Thanks For Playing")
