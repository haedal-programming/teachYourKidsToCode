# yes or no를 입력받자
answer = input("나선형을 보고 싶으세요? y/n:")

# 입력받은 값에 따라 구동되는 프로그램을 달리하자
if answer == 'y':
    print("동작 중입니다...")
    import turtle
    cursor = turtle.Pen()
    cursor.width(2)
    # 나선 그리자
    for x in range(100):
        cursor.forward(x*2)
        cursor.left(89)
print("끝났습니다!")


# 나선형을 그릴건지 값을 입력받자
# 조건에 따라 다른 코드를 실행하자
