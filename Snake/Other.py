from turtle import Turtle, Screen
x = 600
y = 600
wynik = Turtle()
wynik.hideturtle()

def score(points):

    wynik.clear()
    wynik.color("white")
    wynik.shape("turtle")
    wynik.penup()
    wynik.setpos(0,(y//2)-30)
    wynik.pendown()
    wynik.write(f"Score = {points} ",True, "center", ("Arial", 10, "normal"))

def frame():
    frame = Turtle()
    frame.hideturtle()
    frame.penup()
    frame.setpos(-x//2,-y//2)
    frame.color("white")
    frame.pensize(20)
    frame.pendown()
    for i in range(0,4):
        frame.forward(x)
        frame.left(90)