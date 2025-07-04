import random
import time

while True:
    rounds = input('How many problems do you want to solve(1-10)?: ')
    if rounds.isdigit():
        rounds = int(rounds)
        if 1 <= rounds <= 10:
            break
        else:
            print('Enter a number between 1 and 10')
    else:
        print("Invalid character!")

for i in range(rounds):
    operators = ('+','-','*','/')
    first_numb = random.randint(1,100)
    second_numb = random.randint(50,100)
    operators_rand = random.choice(operators)
    playing = input("Are you ready(y)?: ")
    start_time = time.time()
    if playing.lower()[0] != 'y':
        break
    else:

        while True:
            calculations = f'{first_numb}{operators_rand}{second_numb}'
            user_answer = input(f'Problem #{i+1}, what is : {calculations}: ')
            if (user_answer.isdigit() or
                (user_answer.startswith('-') and user_answer[1].isdigit())
                ):
                user_answer = int(user_answer)

            else:
                print("Invalid character, type a number")
                continue

            correct_answer = int(eval(calculations))
            if user_answer == correct_answer :
                print(f"\nGood job,correct answer, it was : {correct_answer}")

                end_time = time.time()
                final_time = round(end_time - start_time, 2)
                print(f'time: {final_time} seconds')
                print('-' * 80)
                break
            else:
                print('Wrong answer')
                trying_again = input('Do you want to try again?: ')
                if trying_again.lower()[0] == 'y':
                    print('continue you are almost')
                    continue
                else:
                    print(f'Bye!!, the right answer was: {correct_answer}')
                    break





