import random
print("Welcome to the number guessing game ")
number_of_try = 0
computer_number = random.randint(1,100)


while True :
    player_guess = input("choose a number between 1 and 100: ")
    if player_guess.isdigit():
        player_guess = int(player_guess)
        if player_guess <= 0 :
            print("Please type a number greater than 0")
            continue
        elif player_guess > 100 :
            print("Please type a number equal or smaller than 100")
            continue
    else :
        print("type a number next time")
        continue

    # conditional greater than or smaller than
    if player_guess < computer_number :
        number_of_try += 1
        print("too small, raise your guess!")
    elif player_guess > computer_number :
        print("too high, decrease your guess!")
        number_of_try += 1
    else:
        number_of_try += 1
        print("\n")
        print("---------------------------------------------------")
        print(f"Good guess, you won!!, it was {computer_number}")
        print(f"you tried: {number_of_try} times")
        print("\n")

        play_again = input("do you want to play again?(y/n): ").lower()
        if play_again == "y":
            computer_number = random.randint(1, 100)
            number_of_try = 0
            continue
        else:
            break
