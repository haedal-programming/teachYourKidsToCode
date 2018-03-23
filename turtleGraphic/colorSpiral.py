# 다양한 형태로 그려보자

import turtle
cursor = turtle.Pen()
turtle.bgcolor("black")
# 거북이 펜 커서 속도 최대
turtle.speed(10)
# 2부터 6 사이의 숫자를 골라서 멋진 도형을 만들 수 있습니다
# sides를 바꿔가며 프로그램을 실행해봅시다.
sides = 6
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
    # 선 색을 바꿉니다
    cursor.pencolor(colors[x%sides])
    # 도형의 변 길이를 설정합니다
    cursor.forward(x * 3/sides + x)
    # 회전하게 만듭니다
    cursor.left(360/sides + 1)
    # 바깥 선이 점점 더 굵게 설정해줍니다
    cursor.width(x*sides/200)

input("수고 하셨습니다 Happy Coding :)")
