import random
import turtle
cursor = turtle.Pen()
cursor.speed(0)
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","gray"]
# 함수 사용 : 임의의 크기와 색, 위치를 가지는 나선형 만들기
def random_spiral():
    cursor.pencolor(random.choice(colors))
    size = random.randint(10,40)
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    cursor.penup()
    cursor.setpos(x,y)
    cursor.pendown()
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)
# 함수를 50번 호출하기 == 나선형 50개 그리기
for n in range(50):
    random_spiral()

# 함수 사용 : 임의의 크기와 색, 위치를 가지는 나선형 만들기
# 함수를 50번 호출하기 == 나선형 50개 그리기

# cursor.left("90")
# print("안녕")
#
# def 함수(매개변수):
