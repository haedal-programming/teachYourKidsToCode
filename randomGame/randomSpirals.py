import random
import turtle
cursor = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green",
          "orange","purple","white","gray"]
for n in range(50):
    # 임의의 크기와 색, 위치를 가지는 나선형 만들기
    # 무작위 색 고르기
    cursor.pencolor(random.choice(colors))
    # 무작위 크기 고르기
    size = random.randint(10,40)
    # 무작위 random(x,y) 위치 계산하기
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    cursor.penup()
    cursor.setpos(x,y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)

# 무작위 색 고르기
# 무작위 위치 계산하기
# 무작위 크기의 나선 그리자
