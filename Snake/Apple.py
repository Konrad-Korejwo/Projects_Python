from turtle import Turtle, Screen
from movements import *
import random
x = 600
y = 600

def respawn_apple(x,y):
    apple.hideturtle()
    apple.goto(get_new_position(x,y))
    apple.showturtle()

def get_new_position(x, y):
    is_ok = False
    while not is_ok:
        a = random.randint(-(x//40)-1, (x//40)-1)
        b = random.randint(-(y//40)-1, (y//40)-1)
        xcor = a * 20
        ycor = b * 20
        new_pos = (xcor, ycor)
        is_ok = all(snake.distance(new_pos) >= 20 for snake in snake_body) and -x/2 + 20 < xcor < x/2 - 20 and -y/2 + 20 < ycor < y/2 - 20
    return new_pos



apple = Turtle()
apple.hideturtle()
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(get_new_position(x,y))
apple.showturtle()