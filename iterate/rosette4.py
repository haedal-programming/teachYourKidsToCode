import turtle
cursor = turtle.Pen()

# x에 1,2,3,4 순으로 입력하고 반복한다
# range 의미를 검색해보자
for x in range(4):
    # 반지름 100px인 원을 그리고
    cursor.circle(100)
    # 90도 회전
    cursor.left(90)
    # 360도 / 90도 = 4이므로
    # 4개의 원이 대칭적으로 그려질 것이다
# for 반복 완료
