#  나선형 원을 그려봅니다

import turtle
cursor = turtle.Pen()
# 시간이 오래 걸리면 'range(100)'을 'range(1,100,3)'으로 고쳐봐요
for x in range(100):
    cursor.circle(x)
    # 90도를 91도로 변경합니다. 바뀌는 걸 지켜봐요
    cursor.left(91)

input("Press enter to exit")
