import turtle
cursor = turtle.Pen()
# 사용자에게 측면 수 또는 원의 수를 묻습니다. 기본값은 6입니다.
number = int(turtle.numinput("Number of sides or circles",
            "몇 개의 변 또는 원이 있습니까?", 6))
# 다각형을 그리기 원하는지 아니면 장미 모양을 원하는지 묻습니다
shape = turtle.textinput("어떤 모양을 원하세요?",
                    "다각형은 'p', 장미 모양은 'r'을 입력하세요:")
for x in range(number):
    if shape == 'r':         # 장미 모양을 선택한 경우
        cursor.circle(100)
    else:                    # 기본값은 다각형
        cursor.forward(150)
    cursor.left(360/number)


# 사용자에게 측면 수 또는 원의 수 묻기. 기본값은 6
# 다각형을 원하는지 장미 모양을 원하는지 묻습니다
# 조건에 맞춰 그립니다
