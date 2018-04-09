# 터틀 그래픽 가져오기
import turtle
cursor = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange",
          "purple","white","brown","gray","pink"]
family = []

# while문 특성 때문에 첫번째 입력은 따로 물어야한다
name = turtle.textinput("나의 가족",
                        "이름을 입력하세요. 끝내려면 [ENTER] 키를 누르세요:")
# 이름 반복해 묻기
while name != "":
    # 가족 리스트에 가족 이름 추가하기
    family.append(name)
    # 다른 이름 묻기, 또는 끝내기
    name = turtle.textinput("나의 가족",
                            "이름을 입력하세요. 끝내려면 [ENTER] 키를 누르세요:")

# 이름 가지고 나선형 모양 그리기
for x in range(100):
    # 여러 색을 돌려가며 사용하기
    cursor.pencolor(colors[x%len(family)])
    # 선은 그리지 않기. 이름만 보여줄겁니다!
    # 헷갈리면 penup을 pendown으로 바꿔 실행해봐요!
    cursor.penup()
    # 거북이만 다른 위치로 옮기기
    cursor.forward(x*4)
    # 가족 이름 그리기 준비
    cursor.pendown()
    # 가족 이름 쓰기
    cursor.write(family[x%len(family)],font=("Arial",int((x+4)/4),"bold"))
    # 왼쪽으로 회전하자
    cursor.left(360/len(family) + 2)

# 반복해서 이름 묻기
# 나선으로 표현하기
