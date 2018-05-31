"""컬러 나선형을 그리는 모듈"""
import turtle
def cSpiral(sides=6,size=360,x=0,y=0):
    """ 검정 배경색에 컬러 나선형 그리기.
    인수:
    sides -- 측면의 수(default 6)
    size -- 마지막 변의 길이(초깃값 360)
    x,y -- 화면 가운데를 기준으로 한 나선형의 위치
    """
    cursor=turtle.Pen()
    cursor.speed(0)
    cursor.penup()
    cursor.setpos(x,y)
    cursor.pendown()
    turtle.bgcolor("black")
    colors=["red","yellow","blue","orange","green","purple"]
    for n in range(size):
        cursor.pencolor(colors[n%sides])
        cursor.forward(n * 3/sides + n)
        cursor.left(360/sides + 1)
        cursor.width(n*sides/100)


#
