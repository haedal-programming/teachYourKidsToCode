# 이름과 나이를 입력하고 원하는 문자열 출력해보자

# 변수는 프로그램이 실행되는 동안 무언가를 기억하기 위한 장소입니다.
# 기억한다는건 컴퓨터 메모리에 정보를 저장한다는 의미입니다.
# 변수에 정보를 저장하는 방법
# 변수 = 정보
my_name = "해달"
my_age = 2

# input은 사용자가 입력하는 값을 변수에 할당합니다.
# input 안의 "이름이 뭐야?"는 prompt로써 사용자가 편리하게 사용하도록 합니다.
your_name = input("이름이 뭐야?")
your_age = input("몇 살이야?")

# print 안에서 문자열과 변수를 섞어 사용할 수 있습니다.
print("내 이름은", my_name, "이야. 나는", my_age, "살이야.")
print("너의 이름은 ", your_name, "이고 ", your_age, "살이야.")
print("내 수업을 들어서 고마워, ",your_name, "!")
