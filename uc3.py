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

    # Print the result of the player's turn
    print(f"You rolled a {die_roll} and got a {option}, your new position is {player_position}")

    # Ask the player if they want to continue playing
    choice = input("Do you want to continue playing? (Y/N) ")
    if choice.lower() != "y":
        break

print("Thanks For Playing")
