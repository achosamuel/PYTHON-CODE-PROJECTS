import turtle
import random

colors_list = ['green', 'yellow', 'purple', 'red', 'pink', 'brown']


def set_screen():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.title('Turtle Racing!!')


def draw_finish_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.penup()
    line.goto(-200, -200)
    for _ in range(17):
        line.pendown()
        line.forward(15)
        line.penup()
        line.forward(10)


def draw_label():
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.goto(0, -230)
    label.write("🏁 FINISH LINE 🏁", align="center",
                font=("arial", "18", "bold"))


def create_racers(colors):
    turtles = []
    x = -200
    for color in colors:
        T = turtle.Turtle()
        T.color(color)
        T.shape('turtle')
        T.penup()
        T.goto(x, 230)
        T.right(90)
        T.pendown()
        x += 68

        turtles.append(T)

    return turtles


def turtle_race(turtles):
    while True:
        # T = turtle.Turtle()
        for T in turtles:
            T.forward(random.randint(5, 20))
            if T.ycor() <= -200:
                return T.color()[0]


def announce_winner(winner):
    announce = turtle.Turtle()
    announce.hideturtle()
    announce.penup()
    announce.goto(0, 0)
    announce.write(f"winner = {winner.upper()}", align="center", font=(
        "times new roman", "16", "italic"))


def main():
    set_screen()
    draw_finish_line()
    draw_label()
    random.shuffle(colors_list)
    turtles = create_racers(colors_list)
    winner = turtle_race(turtles)
    announce_winner(winner)

    turtle.done()


main()
