import turtle
cursor = turtle.Pen()
# 측면 수를 사용자에게 묻습니다. 초깃값은 4입니다.
sides = int(turtle.numinput("Number of sides",
            "몇 개의 변을 나선형에 사용합니까?", 4))
# 다각형과 장미 모양을 그리기 위한 외부 반복(큰 회전). 5부터 75까지 반복합니다.
for x in range(5,75):
    cursor.left(360/sides + 5)
    cursor.width(x//25 + 1)
    # 펜 끄기
    cursor.penup()
    # 다음 회전 위치로 이동하기
    cursor.forward(x*4)
    # 펜을 켜서 그릴 준비하기
    cursor.pendown()
    # 내부 반복: 나선형 외부반복의 짝수 회전 위치에 장미 모양 그리기
    if(x % 2 == 0):
        for y in range(sides):
            cursor.circle(x/3)
            cursor.right(360/sides)
    # 홀수 위치라면 작은 다각형 그리기
    else:
        for y in range(sides):
            cursor.forward(x)
            cursor.right(360/sides)

# 측면 수를 사용자에게 묻습니다. 초깃값은 4입니다.
# 외부 반복(큰 회전)을 만듭니다
# 외부 반복 중 내부 반복을 만듭니다.
# 외부 반복 중 홀짝을 나눠 다른 도형을 그립니다.


# 짝수와 홀수에 따라 다른 코드 실행
# 0부터 number-1 까지 실행
# for m in range(number):
#     if (m % 2 == 0): # m이 짝수인지 확인합니다
#         # 짝수일 때 실행하는 코드
#     else:            # m이 짝수가 아니라면 홀수가 분명합니다
#         # 홀수일 때 실행하는 코드
