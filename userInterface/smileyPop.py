# 파이게임 실행 위한 설정
import pygame
import random

BLACK = (0,0,0)
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("스마일리 터뜨리기")
mousedown = False
keep_going = True
clock = pygame.time.Clock()
pic = pygame.image.load("smiley.png")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
# 파이게임의 모든 sprite를 그룹으로 묶어 처리
sprite_list = pygame.sprite.Group()

class Smiley(pygame.sprite.Sprite):
    pos = (0,0)
    xvel = 1
    yvel = 1
    scale = 100

    # Smiley 클래스의 새로운 객체를 만들때 초기화 함수(생성자)
    def __init__(self,pos,xvel,yvel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pic
        self.scale = random.randrange(10,100)
        self.image = pygame.transform.scale(self.image, (self.scale,self.scale))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0] - self.scale/2
        self.rect.y = pos[1] - self.scale/2
        self.xvel = xvel
        self.yvel = yvel
    # 속도에 맞춰 Smiley 위치를 바꾸고, 경계에 닿았는지 확인
    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.xvel = -self.xvel
        if self.rect.y <= 0 or self.rect.y > screen.get_height() - self.scale:
            self.yvel = -self.yvel

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 왼쪽 마우스 버튼이 눌리면 스마일리 그리기
            if pygame.mouse.get_pressed()[0]:
                mousedown = True
            # 오른쪽 마우스 버튼이 눌리면 터뜨리기
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                # []는 s들을 원소로 갖는 배열입니다.
                clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                sprite_list.remove(clicked_smileys)
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    screen.fill(BLACK)
    # 움직이는 sprite들을 screen에 그립니다
    sprite_list.update()
    sprite_list.draw(screen)
    # 초당 60프레임으로 동작
    clock.tick(60)
    # 위의 상황에 맞춰 디스플레이 보여주기
    pygame.display.update()
    # 마우스가 눌리면
    if mousedown:
        # 임의의 속도로 움직이는 스마일리 만들기
        speedx = random.randint(-5,5)
        speedy = random.randint(-5,5)
        newSmiley = Smiley(pygame.mouse.get_pos(),speedx,speedy)
        sprite_list.add(newSmiley)

pygame.quit()

# 파이게임 실행 위한 설정
# 스마일리 클래스로 새로운 스마일리 객채와 움직임 표현하기
# 왼쪽 마우스가 눌릴 때 스마일리 생성하고
# 오른쪽 마우스 눌릴 때 스마일리 삭제하기
