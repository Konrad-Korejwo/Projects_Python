from turtle import Turtle, Screen

x = 600
y = 600

snake_body = []

def new_body():

    for i in range(0,3):
        snake = Turtle()
        snake.penup()
        snake.speed(8)
        snake.shape("square")
        snake.shapesize(0.8)
        snake.color("white")
        snake.setpos((i-1)*(-20), 0 )
        snake_body.append(snake)
    return snake_body

def move():
    head = snake_body[0].position()
    snake_body[0].forward(20)
    for i in range(1, len(snake_body)):
        prev_position = snake_body[i].position()
        snake_body[i].goto(head)
        head = prev_position
    return snake_body



def new_segment():
    new = Turtle()
    new.penup()
    new.speed(8)
    new.shape("square")
    new.shapesize(0.8)
    new.color("white")
    tail = snake_body[-1].position()
    new.goto(tail)
    snake_body.append(new)
    return snake_body

def left():
    snake_body[0].left(90)

def right():
    snake_body[0].right(90)

def check_collision_apple(apple):
    return snake_body[0].distance(apple) < 1

def check_collision_body():
    head_position = snake_body[0].position()
    for segment in snake_body[1:]:
        if segment.distance(head_position) < 1:
            return True
    return False

def check_collision_frame():
    head_x = snake_body[0].xcor()
    head_y = snake_body[0].ycor()
    max_x = x//2-20
    max_y = y//2-20
    if head_x > max_x or head_x < -max_x or head_y > max_y or head_y < -max_y:
        return False
    else:
        return True
