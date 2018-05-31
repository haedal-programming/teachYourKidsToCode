import turtle
cursor = turtle.Pen()
cursor.speed(10)
# 커서 숨기기
cursor.hideturtle()
def draw_face():
    # 얼굴 테두리 색 yellow
    cursor.pencolor("yellow")
    # 얼굴 배경 색 yellow
    cursor.fillcolor("yellow")
    # 배경색 채우기 시작
    cursor.begin_fill()
    # 얼굴 반지름 50
    cursor.circle(50)
    # 배경색 채우기 끝
    cursor.end_fill()
def draw_mouth(x,y):
    # 왼쪽 입꼬리 위 (-25,40)에서 시작
    cursor.setpos(x-25, y+40)
    # 입은 검은색
    cursor.pencolor("black")
    # 두께는 10
    cursor.width(10)
    # 왼쪽 꺾이는 구간 (-10,20)으로 이동
    cursor.goto(x-10, y+20)
    # 오른쪽 꺾이는 구간 (10,20)으로 이동
    cursor.goto(x+10, y+20)
    # 오른쪼 입꼬리 위 (25,40)으로 이동
    cursor.goto(x+25, y+40)
    # 커서 두깨 원래대로
    cursor.width(1)
    # 얼굴 눈 입 합칠때 이거 없으면 이상해집니다

# 얼굴 그리자
draw_face()
# 얼굴 기준 (0,0)에 맞춰 입 그리자
draw_mouth(0,0)


#
