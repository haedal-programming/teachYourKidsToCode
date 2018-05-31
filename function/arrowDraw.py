# 거북이 가져오기
import turtle
cursor = turtle.Pen()
cursor.speed(0)
cursor.turtlesize(2,2,2)
# 방향 설정
def up():
    cursor.forward(50)
def left():
    cursor.left(90)
def right():
    cursor.right(90)
# 방향키 설정
turtle.onkeypress(up,"Up")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
# 사용자 입력 받을 준비
turtle.listen()


# 거북이 가져오기
# 방향 설정
# 방향키 설정
# 사용자 입력 받을 준비
