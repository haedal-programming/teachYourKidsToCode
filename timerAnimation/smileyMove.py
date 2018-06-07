import pygame
pygame.init()
screen = pygame.display.set_mode([600,600])
keep_going = True
pic = pygame.image.load("smiley.png")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
# 에니메이션에 사용할 타이머
timer = pygame.time.Clock()

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        # 그림 옮기기
        picx += 1
        picy += 1

        # 화면 지우기
        screen.fill(BLACK)
        screen.blit(pic,(picx,picy))
        pygame.display.update()
        # 초당 60프레임으로 제한
        timer.tick(60)

pygame.quit()
