# 사각형을 반복해 그려 미로형태를 만듭니다

# 터틀 그래픽의 그리기 능력을 가져오는 명령입니다
import turtle

# cursor라는 글자를 이용해 거북이가 가진 펜을 사용하겠다고 컴퓨터에게 알려줍니다
cursor = turtle.Pen()

# 반복문을 이용해 몇가지 명령을 반복해 실행하는 코드입니다.
# 변수 x는 0 부터 99까지의 범위를 설정해서 반복하고 있습니다. 즉 100번 반복합니다
for x in range(100):
    # 왼쪽의 들여쓰기, 즉 공백이 왼쪽에 있습니다.
    # 해당 코드들이 반복 안에 포함된다는 것을 의미합니다
    # 거북이가 x만큼 앞으로 갑니다
    cursor.forward(x)
    # 왼쪽으로 90도 회전합니다.
    cursor.left(90)

import turtle
cursor = turtle.Pen()
for x in range(100):
    cursor.forward(x)
    cursor.left(90)
