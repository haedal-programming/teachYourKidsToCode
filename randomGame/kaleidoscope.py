import random
import turtle
cursor = turtle.Pen()
cursor.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue","green", "orange","purple","white","gray"]
for n in range(50):
    # 나선형의 색을 결정
    cursor.pencolor(random.choice(colors))
    # 나선형 크기 결정
    size = random.randint(10,40)
    # 제 1사분면에서 무작위(x,y) 위치 생성하기
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)
    # 첫 번째 나선형 그리기 - 제 1사분면
    cursor.penup()
    cursor.setpos(x,y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)
    # 두 번째 나선형 그리기 - 제 2사분면
    cursor.penup()
    cursor.setpos(-x,y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)
    # 세 번째 나선형 그리기 - 제 3사분면
    cursor.penup()
    cursor.setpos(-x,-y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)
    # 네 번째 나선형 그리기 - 제 4사분면
    cursor.penup()
    cursor.setpos(x,-y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)

# 나선형의 임의의 크기와 색을 결정합니다
# 제 1사분면에서의 위치를 결정하고 그립니다.
# 대칭적으로 제 2,3,4사분면 위에도 그립니다
