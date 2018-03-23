#  화려한 나선형 원을 그려봅니다

import turtle
turtle.speed(10)
cursor = turtle.Pen()

# 배경색을 검은색으로 설정합니다
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
    cursor.pencolor(colors[x%4])
    # 지름이 x인 원을 그립니다
    cursor.circle(x)
    # 원을 회전합니다
    cursor.left(91)

input("Press enter to exit ;)")
