# 숫자 하나 바꿔 계단 니선을 만듭니다

import turtle
cursor = turtle.Pen()
for x in range(100):
    cursor.forward(x)
    # 90도를 91도로 변경합니다. 바뀌는 걸 지켜봐요
    cursor.left(91)

# 자동으로 종료되는걸 막아줍니다
input("Press enter to exit ;)")
