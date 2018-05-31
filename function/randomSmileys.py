import random
import turtle
cursor = turtle.Pen()
cursor.speed(10)
cursor.hideturtle()
turtle.bgcolor("black")
# 얼굴 그리기
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
# 눈 그리기
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
# 입 그리기
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
# 스마일리 그리기
def draw_smiley(x,y):
    cursor.penup()
    cursor.setpos(x,y)
    cursor.pendown()
    # 얼굴
    draw_face()
    # 눈
    draw_eyes(x,y)
    # 입
    draw_mouth(x,y)

# 임의의 위치에 50개 그리기
for n in range(50):
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    draw_smiley(x,y)


# 스마일리 그리기 함수 만들고
# 임의의 위치에 50개 그리기
