import random
import turtle
cursor = turtle.Pen()
cursor.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue","green", "orange","purple","white","gray"]
for n in range(50):
    # 임의의 크기와 색을 가진 나선형을 임의의 위치에 그립니다
    # colors[]에서 무작위로 색 고르기
    cursor.pencolor(random.choice(colors))
    # 10부터 40사이의 나선형 크기를 무작위로 고르기
    size = random.randint(10,40)
    # 화면상의 무작위(x,y) 위치 생성하기
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)
    # 첫 번째 나선형
    cursor.penup()
    cursor.setpos(x,y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)
    # 두 번째 나선형
    cursor.penup()
    cursor.setpos(-x,y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)
    # 세 번째 나선형
    cursor.penup()
    cursor.setpos(-x,-y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)
    # 네 번째 나선형
    cursor.penup()
    cursor.setpos(x,-y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)