import random
choices = ["가위","바위","보"]
print("가위가 보를 이깁니다. 보가 바위를 이깁니다. 바위가 가위를 이깁니다.")
player = input("가위,바위,보 중 하나를 선택해주세요 (또는 quite으로 게임을 종료합니다)")
# 사용자가 quit을 입력하기 전까지 게임을 계속합니다.
while player != "quit":
    # 가위, 바위, 보 중 하나를 선택합니다.
    computer = random.choice(choices)
    print("여러분이 선택한 것은 " + player + ", 컴퓨터가 선택한 것은 "+ computer + "입니다.")
    # 같은 것을 낸 경우
    if player == computer:
        print("동점입니다!")
    # 가위가 보를 이깁니다
    elif player == "가위":
        if computer == "보":
            print("여러분이 이겼습니다!")
        else:
            print("컴퓨터가 이겼습니다!")
    # 보가 바위를 이깁니다
    elif player == "보":
        if computer == "바위":
            print("여러분이 이겼습니다!")
        else:
            print("컴퓨터가 이겼습니다!")
    # 바위가 가위를 이깁니다
    elif player == "바위":
        if computer == "가위":
            print("여러분이 이겼습니다!")
        else:
            print("컴퓨터가 이겼습니다!")
    else:
        print("에러가 발생했습니다...")
    print()     # 한 줄 비우기
    # 사용자가 quit을 입력하기 전까지 게임을 계속합니다.
    player = input("가위, 바위, 보 중 하나를 선택해주세요(또는 quit으로 게임을 종료합니다)")

# 사용자가 quit을 입력하기 전까지 게임을 계속합니다
# 사용자와 컴퓨터가 가위, 바위, 보 중 하나를 선택합니다.
# 결과를 출력합니다
