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
# 얼굴 그리자
draw_face()


#
