import random
# 반복 게임
keep_going = True
while keep_going:
    # 다섯 개의 주사위를 무작위로 던지기
    # 다섯 개의 주사위값을 저장하기 위한 배열 설정하기
    dice = [0,0,0,0,0]
    # 다섯 개의 주사위를 던져서 1부터 6사이의 무작위값 저장하기
    for i in range(5):
        dice[i] = random.randint(1,6)
    # 오름차순으로 정렬하기
    dice.sort()
    # 주사위 값 출력하기
    print("던진 주사위 결과는 다음과 같습니다 ", dice)
    # 몇 개의 주사위가 같은지 비교하기
    # 다섯 개의 주사위가 모두 같은 경우
    if dice[0] == dice[4]:
        print("다섯 개가 같습니다!!")
    # 네 개가 같은 경우 - 처음 네 개가 같거나 마지막 네 개가 같은 경우
    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print("네 개가 같습니다!")
    # 세 개가 같은 경우 - 처음 세 개, 가운데 세 개, 마지막 세 개가 같은 경우
    elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
        print("세 개가 같습니다")
    else:
        print("쓸모 없는 조합이군요")
    # 반복할지 묻기
    keep_going = (input("[ENTER] 키를 눌러서 게임을 계속하거나 아무 키나 눌러 종료해주세요:") == "")


# 주사위를 5번 던집니다
# 오름차순으로 정렬합니다
# 몇 개의 주사위가 같은지 비교합니다
# 반복할지 묻습니다
