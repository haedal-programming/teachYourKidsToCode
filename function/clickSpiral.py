import random
import turtle

cursor = turtle.Pen()
cursor.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow","blue","green",
          "orange","purple","white","gray"]
def spiral(x,y):
    cursor.pencolor(random.choice(colors))
    size = random.randint(10,40)
    cursor.penup()
    cursor.setpos(x,y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)
turtle.onscreenclick(spiral)
