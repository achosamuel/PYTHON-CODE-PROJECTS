import random

print("-"*80)
print("Welcome to the rock, paper or scissor game, have fun!!")
print("\n")

choices = ['rock','paper','scissor']
user_wins = 0
computer_wins = 0

while True:
    computer_pick = random.choice(choices)
    user_input = input("type rock/paper/scissor or q to quit: ").lower()
    if user_input[0] == "q":
        print("GoodBye")
        break
    if user_input[0] not in ['r','p','s'] :
        print("choice invalid, choose between rock,paper,scissor")
        continue
    print(f"computer picked: {computer_pick.upper()}")
    print(f"You picked: {user_input.upper()}")

    #conditional to determine winner

    if user_input[0] == computer_pick[0] :
        print("Tie, you have played the same")
        print("\n")
    elif (user_input[0] == 'r' and computer_pick[0] == 's') or \
        (user_input[0] == 's' and computer_pick[0] == 'p') or \
        (user_input[0] == 'p' and computer_pick[0] == 'r') :
        user_wins += 1
        print("You win !!")
        print("\n")
    else:
        computer_wins += 1
        print("You lose")
        print("\n")
    play_again = input("do you want to play again(y/n)?: ").lower()[0]
    if play_again == 'y' :
        continue
    else:
        print("\n")
        print('-'*80)
        print(f"you win {user_wins} games and lose {computer_wins}")
        print("good bye")
        break
