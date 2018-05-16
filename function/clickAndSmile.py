import random
import turtle
cursor = turtle.Pen()
cursor.speed(0)
cursor.hideturtle()
turtle.bgcolor("black")
def draw_smiley(x,y):
    cursor.penup()
    cursor.setpos(x,y)
    cursor.pendown()
    # 얼굴
    cursor.pencolor("yellow")
    cursor.fillcolor("yellow")
    cursor.begin_fill()
    cursor.circle(50)
    cursor.end_fill()
    # 왼쪽 눈
    cursor.setpos(x-15,y+60)
    cursor.fillcolor("blue")
    cursor.begin_fill()
    cursor.circle(10)
    cursor.end_fill()
    # 오른쪽 눈
    cursor.setpos(x+15,y+60)
    cursor.begin_fill()
    cursor.circle(10)
    cursor.end_fill()
    # 입
    cursor.setpos(x-25, y+40)
    cursor.pencolor("black")
    cursor.width(10)
    cursor.goto(x-10, y+20)
    cursor.goto(x+10, y+20)
    cursor.goto(x+25, y+40)
    cursor.width(1)
turtle.onscreenclick(draw_smiley)
