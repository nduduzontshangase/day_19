from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
turtles = []

# create multiple turtles and give each their own positions, then add each to a list
pos = 0
for _ in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[_])
    t.penup()
    t.goto(x=-230, y=-100 + pos)
    pos += 40
    turtles.append(t)

# if user entered a color the game begins
if user_bet:
    race_on = True

while race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
