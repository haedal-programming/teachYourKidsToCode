# pygame 가져오기
# 설정 : 파이게임 시작 + 창 만들기 + 이미지 불러오기
import pygame
pygame.init()
# 창 만들기
screen = pygame.display.set_mode([800,600])
keep_going = True
# 이미지 파일 불러오기
pic = pygame.image.load("smiley.png")
# 게임용 반복처리 : 창 종료 이벤트 + 이미지 그리기
# keep_going이 True인 동안 계속 실행
while keep_going:
    for event in pygame.event.get():
        # 사용자가 창 종료 버튼을 클릭한다면
        if event.type == pygame.QUIT:
            # 게임용 반복 종료
            keep_going = False
    # blit() 메소드는 불러온 이미지 파일을
    # 원하는 위치:  화면(100,100)에 그립니다
    screen.blit(pic, (100,100))
    # 위의 변경사항을 화면에 반영
    pygame.display.update()

# 종료
pygame.quit()


# 설정 : 파이게임 시작 + 창 만들기 + 이미지 불러오기
# 게임용 반복처리 : 창 종료 이벤트 + 이미지 그리기
# 종료
