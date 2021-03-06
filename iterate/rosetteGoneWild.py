import turtle
cursor = turtle.Pen()

# 사용자에게 사용할 원의 수를 묻습니다. 기본값은 6으로 설정합니다
number_of_circles = int(turtle.numinput("Number of circles",
                                        "장미에 몇개의 원을 그리기 원하세요?", 6))

# 입력한 숫자만큼 반복합니다. 1,2,...,number_of_circles
for x in range(number_of_circles):
    # 반지름 100px인 원을 그리고
    cursor.circle(100)
    # 원이 대칭적으로 그려지게 합니다
    cursor.left(360/number_of_circles)

# 사용자 입력 받자. 기본값은 6
# 원을 그리고 회전을 입력받은 수만큼 반복
