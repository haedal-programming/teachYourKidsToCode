# 메시지를 받습니다
message = input("암호화 또는 해독할 메시지를 입력하세요: ")
# 모두 대문자로 변경합니다
message = message.upper()
# 변환 결과를 저장할 빈 문자열을 만듭니다
output = ""
# 메시지를 한 글자씩 읽습니다
for letter in message:
    # 글자가 알파벳 대문자인지 확인합니다
    if letter.issupper():
        # 글자값이 13 증가(이동)합니다
        value = ord(letter) + 13
        # 값을 다시 글자로 변환합니다
        letter = chr(value)
        # 변환할 값이 알파벳 대문자가 아니라면
        if not letter.issupper():
            # Z -> A로 한 바퀴 돈 것이기 때문에 원 상태로 설정합니다
            value -= 26
            # 글자값에서 26을 빼 원 상태로 만듭니다
            letter = chr(value)
    # 변환할 글자를 출력할 문자열을 추가합니다
    output += letter
#변환할 전체 문자열을 출력합니다
print("Output message: ", output)


#
