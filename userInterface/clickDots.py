# 파이게임 실행 위한 설정
import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("그림을 그리려면 클릭하세요")
keep_going = True
RED = (255,0,0)
radius = 15

# 게임 반복
while keep_going:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        # 만약 마우스가 눌리면
        if event.type == pygame.MOUSEBUTTONDOWN:
            spot = event.pos
            # 빨간 원을 그리자
            pygame.draw.circle(screen, RED, spot, radius)
    pygame.display.update()

pygame.quit()


# 파이게임을 실행 위한 설정
# 만약 마우스가 눌리면:
#     빨간 원을 그리자
