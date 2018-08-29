# 설정
import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
pic = pygame.image.load("smiley.png")
picx = 0
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()
# 수평이동과 수직이동 속도
speedx = 5
speedy = 5
# 게임용 반복 처리
while keep_going:
    # 창 종료 이벤트
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    # 수평, 수직 이동 속도에 따라 그림 이동
    picx += speedx
    picy += speedy
    # 창 경계에서 충돌을 감지하면 방향 전환
    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0 or picy + pic.get_height() >= 600:
        speedy = -speedy

    # screen.fill(BLACK)
    screen.blit(pic, (picx,picy))
    pygame.display.update()
    timer.tick(60)
pygame.quit()

# 설정 : 파이게임 시작 + 창 만들기 + 이미지 불러오기
# 게임용 반복처리 : 창 종료 이벤트 + 이미지 옮기기(60fps)
#     창 가장자리에서 충돌하면 수평 혹은 수직 속도 방향 전환
# 종료
