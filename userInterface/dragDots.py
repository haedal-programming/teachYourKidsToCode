# 파이게임 실행 위한 설정
import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("그림을 그리려면 클릭하세요")
keep_going = True
YELLOW = (255,255,0)
radius = 15
mousedown = False

# 게임 반복
while keep_going:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        # 마우스가 눌렸는지 확인
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        # 마우스가 떼졌는지 확인
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    # 마우스가 눌리면
    if mousedown:
        spot = pygame.mouse.get_pos()
        # 노란색 원 그리기
        pygame.draw.circle(screen, YELLOW, spot, radius)
    pygame.display.update()

pygame.quit()


# 파이게임 실행을 위한 설정
# 민약 마우스가 드래그 된다면:
#     해당 위치에 노란색 원 그리기
