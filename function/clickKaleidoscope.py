import random
import turtle
cursor = turtle.Pen()
cursor.speed(0)
cursor.hideturtle()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green",
          "orange","purple","white","gray"]
# 반사 효과를 만드는 만화경 함수
def draw_kaleido(x,y):
    cursor.pencolor(random.choice(colors))
    size = random.randint(10,40)
    draw_spiral(x,y,size)
    draw_spiral(-x,y,size)
    draw_spiral(-x,-y,size)
    draw_spiral(x,-y,size)
# 나선형 그리는 함수
def draw_spiral(x,y,size):
    cursor.penup()
    cursor.setpos(x,y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(92)
# 클릭하는 위치에 나선형 그리기
turtle.onscreenclick(draw_kaleido)

# 반사 효과를 만드는 만화경 함수
# 나선형 그리는 함수
# 클릭하는 위치에 나선형 그리기
