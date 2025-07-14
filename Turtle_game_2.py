import turtle
import random
import time

# variables
MIN_RACERS = 2
MAX_RACERS = 10
WIDTH, HEIGTH = 500, 500

colors_list = ['red', 'green', 'purple', 'brown', 'blue',
               'orange', 'pink', 'yellow', 'cyan', 'gray', 'teal', 'maroon']

# ask how many turtles to race


def number_of_racers():
    while True:
        number_turtles = input(
            f"Enter q to quit the game. How many turtles you want to race ({MIN_RACERS}-{MAX_RACERS})?: ")
        if number_turtles.isalpha():
            if number_turtles.lower()[0] == 'q':
                print("Good bye!!")
                exit()
        if number_turtles.isdigit():
            number_turtles = int(number_turtles)
            if MIN_RACERS <= number_turtles <= MAX_RACERS:
                break
            else:
                print(f"Enter a number between {MIN_RACERS} and {MAX_RACERS}")
        else:
            print("Invalid character, Enter a number or 'q' to quit the game")

    return number_turtles

# color bet on of the user


def color_bet_on(colors, number_color):
    random.shuffle(colors)
    colors_selected = colors[:number_color]
    for i, color in enumerate(colors_selected):
        print(f'{i} -> {color}')
    while True:
        chosen_color_index = input(
            "Enter the number of the color you want to bet on : ")
        if chosen_color_index.isdigit():
            chosen_color_index = int(chosen_color_index)
            if 0 <= chosen_color_index <= len(colors_selected) - 1:
                chosen_color = colors_selected[chosen_color_index]
                return chosen_color, colors_selected
            else:
                print("Enter a number between 0 and {len(colors) - 1}  ")

        elif chosen_color_index.isalpha():
            if chosen_color_index.lower()[0] == 'q':
                print("Good bye !!")
                break
            else:
                print(
                    f"Invalid character, Enter a number.")
        else:
            print(
                f"Invalid character, Enter a number.")


def set_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGTH)
    screen.title('Turtle Racing game💣')
    screen.bgcolor("lightgray")


def finish_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.penup()
    line.goto(-190, -190)
    for _ in range(26):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(5)


def label_finish():
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.goto(0, -220)
    label.write("🏁 FINISH LINE 🏁", align="center",
                font=("arial", "15", "italic"))


def countdown(color):
    item = turtle.Turtle()
    item.hideturtle()
    item.penup()
    item.goto(0, 0)
    for i in [f"you chose: {color.upper()}", 3, 2, 1, "GO"]:
        item.write(f"{i}", align="center", font=("arial", "30", "bold"))
        time.sleep(1)
        item.clear()


def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        T = turtle.Turtle()
        T.shape('turtle')
        T.color(color)
        T.penup()
        T.goto(-WIDTH // 2 + (i+1) * spacingx, HEIGTH // 2 - 20)
        T.right(90)
        T.pendown()
        turtles.append(T)

    return turtles


def move_turtles(turtles):
    while True:
        for T in turtles:
            T.forward(random.randint(5, 20))
            if T.ycor() <= -190:
                return T.color()[0]


def announce_winner(chosen_color, winner):
    announce = turtle.Turtle()
    announce.hideturtle()
    announce.penup()
    announce.goto(0, 0)
    announce.write(f"the winner is the turtle {winner}", align="center", font=(
        "arial", "20", "bold"))
    time.sleep(2)
    announce.clear()


def check_winning(chosen_color, winner):
    announce = turtle.Turtle()
    announce.hideturtle()
    announce.penup()
    announce.goto(0, 0)
    if chosen_color == winner:
        announce.write("!! YOU WIN🤩🤩 !!",  align="center", font=(
            "arial", "20", "bold"))
    else:
        announce.write("!! YOU LOSE😲😖 !!",  align="center", font=(
            "arial", "20", "bold"))


def main():
    while True:
        playing = input('Do you want to play(y)?: ')
        if playing.isalpha():
            if playing.lower()[0] != 'y':
                exit()
            else:
                number_turtles = number_of_racers()
                chosen_color, colors_selected = color_bet_on(
                    colors_list, number_turtles)
                set_screen()
                finish_line()
                label_finish()
                countdown(chosen_color)
                turtles = create_turtle(colors_selected)
                winner = move_turtles(turtles)
                announce_winner(chosen_color, winner)
                check_winning(chosen_color, winner)
                turtle.Screen().textinput("Play again", "Press Enter to continue...")
        else:
            exit()


main()
