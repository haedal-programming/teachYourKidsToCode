# 단위 변환 함수 선언
def convert_in2cm(inches):
    return inches * 2.54
def convert_lb2kg(pounds):
    return pounds / 2.2
# 단위 입력
height_in = int(input("키를 인치 단위로 입력하세요: "))
weight_lb = int(input("몸무게를 파운드 단위로 입력하세요: "))
# 단위 변환
height_cm = convert_in2cm(height_in)
weight_kg = convert_lb2kg(weight_lb)
# 탁구공과 내 키, 몸무게 비교하기
ping_pong_tall = round(height_cm / 4)
ping_pong_heavy = round(weight_kg * 1000 / 2.7)
# 결과 보여주기
print("키는",height_in,"인치입니다. 그리고 몸무게는",weight_lb,"파운드입니다.")
print("탁구공 ",ping_pong_tall,"개의 키와 같으며")
print("탁구공 ",ping_pong_heavy,"개의 몸무게와 같습니다.")

# def 함수(매개변수1, 매개변수2):

# 단위 변환 함수 선언
# 단위 입력
# 단위 변환
# 탁구공과 내 키, 몸무게 비교하기
# 결과 보여주기
