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
def draw_eyes(x,y):
    # 왼쪽 눈
    # 눈 위치 설정
    cursor.setpos(x-15,y+60)
    cursor.fillcolor("blue")
    cursor.begin_fill()
    cursor.circle(10)
    cursor.end_fill()
    # 오른쪽 눈
    cursor.setpos(x+15,y+60)
    cursor.begin_fill()
    cursor.circle(10)
    cursor.end_fill()

# 얼굴 그리자
draw_face()
# 얼굴 기준 (0,0)에 맞춰 눈 그리자
draw_eyes(0,0)


#
