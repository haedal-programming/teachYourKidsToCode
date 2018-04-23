import turtle
cursor = turtle.Pen()
# 측면 수를 사용자에게 묻습니다. 초깃값은 4입니다.
sides = int(turtle.numinput("Number of sides",
            "몇 개의 변을 나선형에 사용합니까?", 4))
# 다각형과 장미 모양을 그리기 위한 외부 반복. 5부터 75까지 반복합니다.
for x in range(5,75):
    cursor.left(360/sides + 5)
    cursor.width(x//25 + 1)
    cursor.penup()
    cursor.forward(x*4)
    cursor.pendown()
    # 나선형의 짝수 회전 위치에 장미 모양 그리기
    if(x % 2 == 0):
        for y in range(sides):
            cursor.circle(x/3)
            cursor.right(360/sides)
    # 홀수 위치라면 작은 다각형 그리기
    else:
        for y in range(sides):
            cursor.forward(x)
            cursor.right(360/sides) 
