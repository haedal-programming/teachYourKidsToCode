import turtle
cursor = turtle.Pen()

# 사용자에게 사용할 원의 수를 묻습니다. 기본값은 6으로 설정합니다
number_of_circles = int(turtle.numinput("Number of circles",
                                        "장미에 몇개의 원을 그리기 원하세요?", 6))
turtle.bgcolor("black")
# 첫번째 장미는 빨간색
cursor.color("red")
# 입력한 숫자만큼 반복합니다. 1,2,...,number_of_circles
for x in range(number_of_circles):
    # 반지름 100px인 원을 그리고
    cursor.circle(100)
    # 원이 대칭적으로 그려지게 합니다
    cursor.left(360/number_of_circles)

# 두번째 장미는 노란색
cursor.color("yellow")
for x in range(number_of_circles):
    # 반지름 100px인 원을 그리고
    cursor.circle(50)
    # 원이 대칭적으로 그려지게 합니다
    cursor.left(360/number_of_circles)


# 사용자 입력받자
# 검은색 배경색 추가
# 첫번째 장미는 빨간색
# 반지름 100인 원으로 장미 그리기
# 두번째 장미는 노란색
# 반지른 50인 원으로 장미 그리기
