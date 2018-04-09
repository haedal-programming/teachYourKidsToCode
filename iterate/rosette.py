import turtle
cursor = turtle.Pen()

# 첫번째 원을 그립니다(위쪽)
cursor.circle(100)
# 거북이가 왼쪽으로 90도 회전합니다
cursor.left(90)

# 두번째 원을 그립니다(왼쪽)
cursor.circle(100)
cursor.left(90)

# 세번째 원을 그립니다(아래쪽)
cursor.circle(100)
cursor.left(90)

# 네번째 원을 그립니다(오른쪽)
cursor.circle(100)
cursor.left(90)

# 원을 그리고 90도 회전 * 4
