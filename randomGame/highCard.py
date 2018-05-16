import random
faces = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
suits = ["클럽", "다이아몬드", "하트", "스페이드"]
keep_going = True
while keep_going:
    # 나와 상대방이 카드를 뽑고
    # 내 카드 숫자 무작위로 뽑고
    my_face = random.choice(faces)
    # 내 카드 모양 무작위로 뽑자
    my_suit = random.choice(suits)
    # 상대방 카드 숫자 무작위로 뽑고
    your_face = random.choice(faces)
    # 상대방 카드 모양 무작위로 뽑자
    your_suit = random.choice(suits)

    print("내가 가진 카드는 ", my_face," ", my_suit, "입니다")
    print("당신이 가진 카드는 ", your_face," ", your_suit, "입니다")
    # 카드 숫자를 비교해 승무패를 가린다
    if faces.index(my_face) > faces.index(your_face):
        print("내가 이겼어요!")
    elif faces.index(my_face) < faces.index(your_face):
        print("당신이 이겼어요!")
    else:
        print("비겼습니다")
    # 끝낼지 계속할지 물어본다
    answer = input ("[Enter] 키를 누르면 계속 진행합니다. 종료하려면 아무 키나 누르세요")
    keep_going = (answer == "")

# 나와 상대방이 카드를 뽑고
# 카드 숫자를 비교해 승무패를 가린다
# 끝낼지 계속할지 물어본다
