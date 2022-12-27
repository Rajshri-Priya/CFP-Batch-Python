import random

def rollDie():
    roll = random.randint(1, 6)
    return roll

def generateOption():
    option = random.randint(1, 3)
    if option == 1:
        return "No Play"
    elif option == 2:
        return "Ladder"
    else:
        return "Snake"

print("WELCOME TO SNAKE LADDER GAME")

player1_position = 0
player2_position = 0  # uc7 add second player
num_rolls = 0

while True:
    for player in ["Player 1", "Player 2"]:
        die_roll = rollDie()
        option = generateOption()

        if player == "Player 1":
            if option == "No Play":
                player1_position = player1_position
            elif option == "Ladder":
                player1_position += die_roll
                print(f"{player} got a Ladder and gets to play again!")
                continue
            else:
                player1_position -= die_roll

            if player1_position < 0:
                player1_position = 0
            elif player1_position > 100:
                player1_position = player1_position - die_roll

            print(f"{player} rolled a {die_roll} and got a {option}, their new position is {player1_position}")
            # ---------------------------------player2----------------------------------
        else:
            if option == "No Play":
                player2_position = player2_position
            elif option == "Ladder":
                player2_position += die_roll
                print(f"{player} got a Ladder and gets to play again!")
                continue
            else:
                player2_position -= die_roll

            if player2_position < 0:
                player2_position = 0
            elif player2_position > 100:
                player2_position = player2_position - die_roll

            print(f"{player} rolled a {die_roll} and got a {option}, their new position is {player2_position}")

        num_rolls += 1 # for total rolls for winning
        if player1_position == 100:
            print(f"{player} won the game in {num_rolls} rolls!")
            break
        elif player2_position == 100:
            print(f"{player} won the game in {num_rolls} rolls!")
            break

print("Game Over")