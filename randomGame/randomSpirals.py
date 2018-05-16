import random
import turtle
cursor = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green",
          "orange","purple","white","gray"]
for n in range(50):
    # 임의의 크기와 색, 위치를 가지는 나선형 만들기
    # 무작위 색 고르기
    cursor.pencolor(random.choice(colors))
    # 무작위 크기 고르기
    size = random.randint(10,40)
    # 무작위 random(x,y) 위치 계산하기
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,
                         turtle.window_height()//2)
    # 나선을 그릴 무직위 위치로 이동하자
    # 지금부터 펜을 끕니다
    cursor.penup()
    # (x,y)의 원하는 무작위 위치로 이동합니다
    cursor.setpos(x,y)
    # 이동후 원하는 자리에 왔으니 펜을 켭니다
    cursor.pendown()
    # 나선형 그리기
    for m in range(size):
        cursor.forward(m*2)
        cursor.left(91)

# 무작위 색 고르기
# 무작위 위치 계산하기
# 무작위 크기의 나선 그리자

# import turtle
# cursor = turtle.Pen()
# # 지금부터 펜을 끕니다
# cursor.penup()
# # (x,y)의 원하는 위치로 이동합니다
# cursor.setpos(x,y)
# # 지금부터 그림을 그릴거니 펜을 켭니다
# cursor.pendown()

# import random
# import turtle
#
# # // 연산자는 나눗셈에서 몫을 구할때 사용합니다.
# x = random.randrange(-turtle.window_width()//2,
#                       turtle.window_width()//2)
# y = random.randrange(-turtle.window_height()//2,
#                       turtle.window_height()//2)
