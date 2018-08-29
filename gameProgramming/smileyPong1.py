# 파이게임 실행 위한 설정
import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Smiley Pong")
keepGoing = True
# 스마일리 그림을 불러옵니다
pic = pygame.image.load("smiley.png")
# 그림의 흰색 배경을 잘라냅니다
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
# 스마일리의 출발점은 (0,0)
picx = 0
picy = 0
BLACK = (0,0,0)
WHITE = (255,255,255)

# 초당 프레임 설정 위한 준비
timer = pygame.time.Clock()
# 스마일리 속도
speedx = 5
speedy = 5
# 탁구체 크기
paddlew = 200
paddleh = 25
paddlex = 300
paddley = 550
# 스마일리 크기
picw = 100
pich = 100

# 점수와 생명
points = 0
lives = 5
# 폰트
font = pygame.font.SysFont("Times",24)

# 게임 시작
while keepGoing:
    # 종료 버튼을 누른다
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
    # 움직이는 그림
    picx += speedx
    picy += speedy
    # 화면 경계에서 벽과 스마일리 충돌 처리
    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0:
        speedy = -speedy
    # 스마일리가 바닥에 닿는 경우
    if picy >= 500:
        lives -= 1
        speedy = -speedy
    screen.fill(BLACK)
    screen.blit(pic, (picx,picy))

    # 탁구채 그리기
    paddlex = pygame.mouse.get_pos()[0]
    paddlex -= paddlew/2
    pygame.draw.rect(screen, WHITE, (paddlex,paddley,paddlew,paddleh))

    # 탁구채가 공을 쳤는지 확인
    # y축상에서 탁구채 사이에 스마일리가 존재하는지 확인
    if picy + pich >= paddley and picy + pich <= paddley + paddleh and speedy > 0:
        # x축상에서 탁구채 사이에 스마일리가 존재하는지 확인
        if picx + picw / 2 >= paddlex and picx + picw / 2 <= paddlex + paddlew:
            # 스마일리와 탁구채가 충돌했으므로 점수를 올리고 스마일리 운동 방향 바꾸기
            points += 1
            speedy = -speedy

    # 점수와 생명을 표시하자
    # 원하는 점수가 적힌 문자열 만들기
    draw_string = "Lives: " + str(lives) + " Points: " + str(points)
    # 투명한 사각형 안에 흰색으로 점수가 적히게 합니다.
    text = font.render(draw_string, True, WHITE)
    # 투명한 사각형을 변수에 집어넣습니다
    text_rect = text.get_rect()
    # 화면의 중앙과 투명한 사각형의 중심을 일치시킵니다
    text_rect.centerx = screen.get_rect().centerx
    # y축으로 10만큼 내립니다
    text_rect.y = 10
    screen.blit(text,text_rect)
    pygame.display.update()
    timer.tick(60)

pygame.quit()

# 스마일리 퐁을 위한 설정
# 스마일리, 탁구채, 점수판을 그린다
# 스마일리가 벽 혹은 탁구채와 충돌 처리
# 열심히 짜보자
