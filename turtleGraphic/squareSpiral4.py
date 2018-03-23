# 화려한 계단 나선을 만듭니다

import turtle
cursor=turtle.Pen()
# 빨강, 노랑, 파랑, 초록이 들어간 배열을 만듭니다.
# 배열이 어렵다면 목록이라고 생각하세요.
# 색 순서대로 나선이 그려집니다
colors = ["red","yellow","blue","green"]
for x in range(100):
    # 목록에 있는 4가지 색을 순서대로 사용합니다.
    # % 연산자는 나머지를 구합니다.
    cursor.pencolor(colors[x%4])
    cursor.forward(x)
    cursor.left(91)
