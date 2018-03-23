# 이름으로 나션형 모양 그리기

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

# 터틀의 textinput 알림창을 이용해 사용자 이름 묻기
your_name = turtle.textinput("Enter your name", "What is your name?")

# 화면에 이름을 나선형으로 100번 출력하기
for x in range(100):
    t.pencolor(colors[x%4]) # 4개의 색 번갈아 사용하기
    t.penup()               # 일반 나선형 선은 그리지 않는다
    t.forward(x*4)          # 화면에 있는 거북이 움직이기
    t.pendown()             # 사용자 이름을 점점 크게 그리기
    # 이름을 원하는 폰트와 크기로 그린다
    t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold"))
    t.left(92)              # 왼쪽으로 회전
