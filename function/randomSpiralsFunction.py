import random
import turtle
cursor = turtle.Pen()
cursor.speed(0)
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","gray"]
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

for n in range(50):
    random_spiral()                        
