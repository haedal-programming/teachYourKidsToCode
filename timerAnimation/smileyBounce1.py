# 설정
import pygame
pygame.init()
# 창 만들기
screen = pygame.display.set_mode([600,600])
keep_going = True
# 이미지 파일 불러오기
pic = pygame.image.load("smiley.png")
# 이미지 파일은 왼쪽 위에서 시작
picx = 0
picy = 0
# 검은색 설정
BLACK = (0,0,0)
# 애니메이션에 사용할 타이머
timer = pygame.time.Clock()
# 그림이 이동하는 속도
speed = 5

# 게임용 반복 처리
while keep_going:
    # 창 종료 이벤트
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    # 속도에 따라 그림 이동
    picx += speed
    picy += speed
    # 충돌을 감지하면
    if picx <= 0 or picx + pic.get_width() >= 600:
        # 속도 방향 전환
        speed = -speed

    screen.fill(BLACK)
    screen.blit(pic, (picx,picy))
    pygame.display.update()
    # 초당 60프레임으로 제한
    timer.tick(60)

pygame.quit()

# 설정 : 파이게임 시작 + 창 만들기 + 이미지 불러오기
# 게임용 반복처리 : 창 종료 이벤트 + 이미지 옮기기(60fps)
#     충돌하면 속도 방향 전환
# 종료
