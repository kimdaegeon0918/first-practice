import pygame
# from pygame.constants import DROPCOMPLETE

pygame.init() #초기화 반드시 필욭

#화면 크기 설정
screen_width=480 #가로
screen_height=640 #세로
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#fps
clock=pygame.time.Clock()
###################################################
#1.사용자 게임 초기화(배경화면,게임이미지,좌표,속도,폰트 등)

#이벤트 루프
running=True #게임이 진행중인가
while(running):
    dt=clock.tick(60) #게임화면의 초당프레임

    #2. 이벤트 처리(키보드,마우스)
    
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT: #창이 닫히는 이벤트가 발생하면
            running=False

    #3. 게임 캐릭터 위치 정의

    #4. 충돌처리

    #5. 화면에 그리기


    
    pygame.display.update() #게임 화면을 다시 그리기



#pygame 종료
pygame.quit()
