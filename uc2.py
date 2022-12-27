import random
# uc2 ---The Player rolls the die to get a number between 1 to 6. - Use ((RANDOM)) to get the number between 1 to 6

def dieRolling():
    roll = random.randint(1, 6)
    return roll


print("WELCOME TO SNAKE LADDER GAME")
PlayerPosition = 0  # Set the player's starting position
die_roll = dieRolling()
PlayerPosition = die_roll  # Update the player's position based on the die roll
print(f"You rolled a {die_roll}, your new position is {PlayerPosition}")
