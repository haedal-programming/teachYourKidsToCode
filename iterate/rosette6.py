import turtle
cursor = turtle.Pen()

# x에 1,2,3,4,5,6 순으로 입력하고 반복한다
# range 의미를 검색해보자
for x in range(6):
    # 반지름 100px인 원을 그리고
    cursor.circle(100)
    # 60도 회전
    cursor.left(60)
    # 360도 / 60도 = 6이므로
    # 6개의 원이 대칭적으로 그려질 것이다
# 반복 완료

# 원을 그리고 60도 회전 * 6
