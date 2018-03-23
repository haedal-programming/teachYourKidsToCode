#  빨간색 계단 나선을 만듭니다

import turtle
cursor = turtle.Pen()
# 빨간색으로 그려봅니다
cursor.pencolor("red")
for x in range(100):
    cursor.forward(x)
    cursor.left(91)

input("Press enter to exit ;)")
