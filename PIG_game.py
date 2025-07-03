import random

def roll():
    rolling = random.randint(1,6)
    return rolling

while True:
    player_number = input("Enter the number of player 2-4: ")
    if player_number.isdigit():
        player_number = int(player_number)
        if 2 <= player_number <= 4:
            break
        else:
            print("Enter a number between 1 and 4")
    else:
        print("Invalid character")

player_score = [0 for i in range(player_number)]
max_score = 20

while max(player_score) < max_score:
    for player_id in range(player_number):
        print("-"*80)
        print(f'player {player_id +1} turn start')
        current_score = 0

        while True:
            playing = input("Do you want to roll (y/n)?: ")
            if playing.lower() != 'y':
                break

            value = roll()
            if value == 1:
                value = 0
                print(f"\nYou rolled a 1, you lost your turn !")
                print(f"---> total score is: {player_score[player_id]}\n")
                break

            else:
                print(f"you rolled: {value}")

            player_score[player_id] += value
            print(f"Total score is {player_score[player_id]}")

            if player_score[player_id] >= 20:
                break

winner_score = max(player_score)
winner_id = player_score.index(winner_score)
print(f"\n Player {winner_id +1} win this game with {winner_score}!")
