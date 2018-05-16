import turtle
cursor = turtle.Pen()
cursor.speed(0)
cursor.turtlesize(2,2,2)
def up():
    cursor.forward(50)
def left():
    cursor.left(50)
def right():
    cursor.right(50)
turtle.onkeypress(up,"Up")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()
