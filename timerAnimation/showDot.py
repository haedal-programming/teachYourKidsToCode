import pygame

# 파이게임을 시작하겠다
pygame.init()
# 너비 800화소, 높이 600화소의 창을 만든다
screen = pygame.display.set_mode([800,600])

# 반복 변수 keep_going 선언
keep_going = True
# GREEN 변수에 RGB 색상 설정(초록색)
GREEN = (0,255,0)
radius = 50

# 사용자가 "종료" 선택 전까지 계속 반복
while keep_going:
    # 사용자 조작 처리
    for event in pygame.event.get():
        # 사용자가 종료
        if event.type == pygame.QUIT:
            keep_going = False
    # 화면의 (100,100) 위치에 초록색 원 그리기
    pygame.draw.circle(screen, GREEN, (100,100), radius)
    # 변경사항 반영한 애니메이션 보여주기
    pygame.display.update()

# 파이게임 종료
pygame.quit()

# (Red,Green,Blue)
# RED   = (255,0,0)
# GREEN = (0,255,0)
# BLUE  = (0,0,255)
# WHITE = (255,255,255)
# BLACK = (0,0,0)

# 파이게임 시작
# 너비 800화소, 높이 600화소 창 만들기
# 사용자의 종료 조작 처리
# 화면의 (100,100) 위치에 초록색 원 그리기
# 파이게임 종료
