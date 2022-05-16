import pygame
# from pygame.constants import DROPCOMPLETE
from random import * 

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
#배경화면
background=pygame.image.load("C:/Users/velks/Documents/z/python/pygame_basic/background.png")
#게임이미지
character=pygame.image.load("C:/Users/velks/Documents/z/python/pygame_basic/character.png")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-character_width/2
character_y_pos=screen_height-character_height

enemy=pygame.image.load("C:/Users/velks/Documents/z/python/pygame_basic/enemy.png")
enemy_size=enemy.get_rect().size
enemy_width=enemy_size[0]
enemy_height=enemy_size[1]
enemy_x_pos=randrange(0 ,screen_width-enemy_width) #랜덤x위치
enemy_y_pos=0 

#좌표
to_x=0
to_y=0

#속도
character_speed=0.6
enemy_speed=0.6

#폰트
game_font=pygame.font.Font(None,40)


#이벤트 루프
running=True #게임이 진행중인가
while(running):
    dt=clock.tick(30) #게임화면의 초당프레임
    print("fps : "+str(clock.get_fps()))

    if enemy_y_pos>screen_height: #적이 화면밖으로 사라지면
        enemy_x_pos=randrange(enemy_width,screen_width-enemy_width) #재생성
        enemy_y_pos=0 
    
    enemy_y_pos+=enemy_speed*dt #적 아래로 이동

    #2. 이벤트 처리(키보드,마우스)
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT: #창이 닫히는 이벤트가 발생하면
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT: #왼쪽
                to_x-=character_speed
            if event.key==pygame.K_RIGHT: #오른쪽
                to_x+=character_speed
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0

    character_x_pos+=to_x*dt

    #가로경계값
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width

    #4. 충돌처리
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌하였습니다.")
        running=False
    
    #5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    pygame.display.update() #게임 화면을 다시 그리기
    
#pygame 종료
pygame.quit()
