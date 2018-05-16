import random
import turtle
cursor = turtle.Pen()
cursor.speed(0)
cursor.hideturtle()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green",
          "orange","purple","white","gray"]
def draw_kaleido(x,y):
    cursor.pencolor(random.choice(colors))
    size = random.randint(10,40)
    draw_spiral(x,y,size)
    draw_spiral(-x,y,size)
    draw_spiral(-x,-y,size)
    draw_spiral(x,-y,size)
def draw_spiral(x,y,size):
    cursor.penup()
    cursor.setpos(x,y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(92)
turtle.onscreenclick(draw_kaleido)
