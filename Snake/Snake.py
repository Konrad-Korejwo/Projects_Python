from turtle import Turtle, Screen
import movements as m
from movements import *
import time
from Apple import *
from Other import *


screen=Screen()
x = 600
y = 600

screen.screensize(x-10,y-10)
screen.setup(x,y)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

m.new_body()
frame()
is_game_on = True
points = 0

difficulty = int(screen.textinput("WYBIERZ STOPIEŃ TRUDNOŚCI", "Jaki poziom trudności wybierasz?\nŁatwy (1)\nŚredni (2)\nTrudny(3)"))
screen.listen()
speed = 0.2 /difficulty

while is_game_on:
    m.move()
    screen.update()
    if m.check_collision_apple(apple):
        respawn_apple(x,y)
        new_segment()
        points+=1
        score(points)
    if m.check_collision_body():
        is_game_on = False
    if not check_collision_frame():
        is_game_on = False
    screen.update()
    screen.onkey(m.left, "Left")
    screen.onkey(m.right, "Right")
    time.sleep(speed)
    screen.update()

screen.textinput("GAME OVER!", f"Your score: {points}")
screen.exitonclick()