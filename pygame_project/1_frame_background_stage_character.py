import os
import pygame
# from pygame.constants import DROPCOMPLETE

pygame.init() #초기화 반드시 필욭

#화면 크기 설정
screen_width=640 #가로
screen_height=480 #세로
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado PANG") #게임 이름

#fps
clock=pygame.time.Clock()
###################################################
#1.사용자 게임 초기화(배경화면,게임이미지,좌표,속도,폰트 등)

current_path=os.path.dirname(__file__) #현재 파일의 위치
image_path=os.path.join(current_path,"image") #image 폴더 위치

#배경 만들기
background=pygame.image.load(os.path.join(image_path,"background.png"))

#스테이지 만들기
stage=pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size=stage.get_rect().size
stage_height=stage_size[1] #스테이지 높이

#캐릭터 만들기
character=pygame.image.load(os.path.join(image_path,"character.png"))
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-character_width/2
character_y_pos=screen_height-stage_height-character_height


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
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update() #게임 화면을 다시 그리기



#pygame 종료
pygame.quit()
