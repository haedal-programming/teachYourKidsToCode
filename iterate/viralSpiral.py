import turtle
cursor = turtle.Pen()
cursor.penup()
turtle.bgcolor("black")
# 사용자에게 나선에 사용할 측면 수를 묻습니다. 초깃값은 4, 최소값은 2, 최대값은 6
sides = int(turtle.numinput("Number of sides",
            "나선형의 나선형에 사용하기 원하는 측면 수는 몇 개입니까(2~6)?",4,2,6))
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
# 외부 나선형 반복 : a
for a in range(100):
    cursor.forward(a*4)
    position = cursor.position() # 나선형의 회전 위치를 기억합니다
    heading = cursor.heading() # 진행할 방향을 기억합니다
    print(position, heading)
    # 내부 나선형 반복 : b
    # 큰 나선형의 회전 위치에 작은 나선형 그리기
    for b in range(int(a/2)):
        cursor.pendown()
        cursor.pencolor(colors[b%sides])
        cursor.forward(2*b)
        cursor.right(360/sides - 2)
        cursor.penup()
    # 큰 나선형의 x위치로 복귀
    cursor.setx(position[0])
    # 큰 나선형의 y위치로 복귀
    cursor.sety(position[1])
    # 큰 나선형 커서의 원래 방향으로 복귀
    cursor.setheading(heading)
    # 큰 나선형의 다음 위치로 회전
    cursor.left(360/sides + 2)

# 나선에 사용할 측면 수 입력받자
# 큰(1차) 나선 그리며
# 작은(2차) 나선 그리자

# 이것이 첫 번째 반복입니다. 외부(1차) 반복이라 부릅니다
# for x in range(20):
    # 들여쓰기 한 처리가 20번 실행됩니다.
    # 아래는 내부(2차) 반복 또는 내포된 반복이라 부릅니다
#    for y in range(10):
        # 두 번 들여쓰기 한 처리들이 200번(20*10) 실행됩니다
# 두 번 들여쓰기 한 처리가 y번 처리되고,
# 한 번 들여쓰기 한 처리가 x번 처리됩니다.

# for a in range(100):
#     cursor.forward(a*4)
#     # 나선형의 회전 위치를 기억합니다
#     position = cursor.position()
#     # 진행할 방향을 기억합니다
#     heading = cursor.heading()
