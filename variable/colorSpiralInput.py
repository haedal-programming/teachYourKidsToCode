# colorSpiral.py에 입력창 추가

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
# white와 gray를 추가하자
colors = ["red", "yellow", "blue", "orange", "green", "purple","white","gray"]
# 1부터 8사이의 수를 입력받는다. 초깃값은 4
sides = int(turtle.numinput("도형 측면 수", "몇 개의 변을 그리고 싶으세요(1-8)?", 4,1,8))
for x in range(360):
    t.pencolor(colors[x%sides])     # 색 목록 범위 안에서만 색을 선택
    t.forward(x * 3/sides + x)      # 측면 수에 일치시켜 크기를 변경
    t.left(360/sides + 1)           # 360도/sides + 1 만큼 왼쪽으로 회전
    t.width(x*sides/200)            # 펜 크기가 점점 커지도록 설정
