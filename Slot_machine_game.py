🎰 SLOT MACHINE — FULL PROJECT BRIEF

  import random
import time

# constants
MAX_LINES = 3
MIN_LINES = 1

MAX_BET = 200
MIN_BET = 10

ROWS = 3
COLS = 3

# dictionnaries
symbols = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

#create a list that all symbols n times
def build_slot_machine_columns(symbols,rows,cols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] *symbol_count)

    #create our slot machine list that content all columns created randomly
    columns = []
    for i in range(cols):
        column = []
        symbols_no_picked = all_symbols[:]

        for y in range(rows):
            symbol_picked = random.choice(symbols_no_picked)
            symbols_no_picked.remove(symbol_picked)
            column.append(symbol_picked)

        columns.append(column)

    return columns

#display the columns created as a slot machine displaying
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):

            if i == 0:
                print(" +-----+-----+-----+")
                print(' | ',column[row],end='  |  ')

            else:
                print(column[row],end='  |  ')
        print()
        if row == len(columns[0]) -1:
            print(" +-----+-----+-----+")



# ask the user how much to deposit
def deposit():
    while True:
        amount_deposit = input('How much do you want to deposit?: $')
        if amount_deposit.isdigit():
            amount_deposit = int(amount_deposit)
            if amount_deposit == 0:
                print("Your deposit should be greater than 0.")
            else:
                break

        else:
            print("Invalid character, Enter a number.")

    return amount_deposit

# ask the user how many lines to bet on
def get_number_lines():
    while True:
        lines = input(f"You want to bet on how many lines ({MIN_LINES}-{MAX_LINES}), type q to quit: ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES :
               break
            else:
                print(f"Enter a number between {MIN_LINES} and {MAX_LINES}")

        elif lines.lower()[0] == 'q':
            quit()

        else:
            print("Invalid character, Enter a number.")

    return lines

# ask how much to bet on each line
def get_bet_on_each_line():
    while True:
        bet = input(f"How much bet on each lines ({MIN_BET}-{MAX_BET})?: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET :
               break
            else:
                print(f"Enter a number between {MIN_BET} and {MAX_BET}")

        else:
            print("Invalid character, Enter a number.")

    return bet

#check the winning
def check_winning(columns, value, bet):
    winning = 0
    winning_lines = []
    for row in range(len(columns[0])):
        symbol_reference = columns[0][row]

        for i,column in enumerate(columns):
            if symbol_reference != column[row] :
                break
        else:
            winning_lines.append(row +1)
            winning += value[symbol_reference] *bet

    return winning, winning_lines

#max bet option
def max_bet_option():
    max_bet = input("For max click 'y': ")
    if max_bet.lower()[0] == 'y':
        lines = MAX_LINES
        bet_per_line = MAX_BET
    else:
        lines = 0
        bet_per_line = 0

    return lines, bet_per_line



def main():
    payout = input("See the payout rules?:")
    if payout.lower()[0] == 'y':
        for symbol, value in symbol_value.items():
            print(f'symbol {symbol} -> x{value}')

    balance = deposit()
    total_bet = 0
    total_wins = 0
    total_rounds = 0

    while True:
        while True:
            lines, bet_per_line = max_bet_option()
            if lines == 0 :
                lines = get_number_lines()
                bet_per_line = get_bet_on_each_line()
            bet = lines * bet_per_line

            if bet <= balance:
                break
            else:
                print(f"Your balance amount ${balance} cannot support your total bet ${bet}")
        total_bet += bet
        slots = build_slot_machine_columns(symbols,ROWS,COLS)
        print("spinning...")
        print("🎰🎰🎰")
        time.sleep(3)
        print_slot_machine(slots)
        winning, winning_lines = check_winning(slots,symbol_value,bet_per_line)

        total_rounds += 1
        total_wins += winning

        if winning > 0:
            print(f"You won: ${winning}🤑")
            print("You won on lines:",", ".join(str(line) for line in winning_lines))
        else:
            print("💸 You lost this round. Better luck next time!")
        print()


        playing = input('Another round ?: ')
        balance = balance - bet + winning
        if playing.lower()[0] != 'y':
            print(f"Final balance: ${balance}")
            print(f"You bet ${total_bet} and you won ${total_wins}")
            print(f'Total rounds: {total_rounds}')
            quit()
        else:

            print(f">>> Your current balance💰 : ${balance}")
            if balance < MIN_BET:
                print(f"Game over, your balance is not enough to play again, minimum bet on line is ${MIN_BET}")
                break
            else:
                continue


main()




