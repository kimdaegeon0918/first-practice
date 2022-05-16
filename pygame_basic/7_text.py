import pygame
from pygame.constants import DROPCOMPLETE

pygame.init() #초기화 반드시 필욭

#화면 크기 설정
screen_width=480 #가로
screen_height=640 #세로
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#fps
clock=pygame.time.Clock()

#배경 이미지 불러오기
background=pygame.image.load("C:/Users/velks/Documents/z/python/pygame_basic/background.png")

#스프라이트 불러오기
character=pygame.image.load("C:/Users/velks/Documents/z/python/pygame_basic/character.png")
character_size=character.get_rect().size #이미지의 크기 구하기
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2 - character_width/2
character_y_pos=screen_height - character_height
#이동할 좌표
to_x=0
to_y=0
#이동속도
character_speed=0.6

#적 캐릭터
enemy=pygame.image.load("C:/Users/velks/Documents/z/python/pygame_basic/enemy.png")
enemy_size=enemy.get_rect().size #이미지의 크기 구하기
enemy_width=enemy_size[0]
enemy_height=enemy_size[1]
enemy_x_pos=screen_width/2 - enemy_width/2
enemy_y_pos=screen_height/2 - enemy_height/2

#폰트 정의
game_font=pygame.font.Font(None,40)

#총 시간
total_time=10

#시작 시간 
start_ticks=pygame.time.get_ticks()

#이벤트 루프
running=True #게임이 진행중인가
while(running):
    dt=clock.tick(60) #게임화면의 초당프레임
    print("fps : "+str(clock.get_fps()))
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT: #창이 닫히는 이벤트가 발생하면
            running=False

        if event.type==pygame.KEYDOWN : #키가 눌러졌을때
            if event.key==pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x-=character_speed
            elif event.key==pygame.K_RIGHT : #오른쪽
                to_x+=character_speed
            elif event.key==pygame.K_UP : #위
                to_y-=character_speed
            elif event.key==pygame.K_DOWN : #아래
                to_y+=character_speed
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0

    character_x_pos+=to_x*dt
    character_y_pos+=to_y*dt

    #가로 경계값
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
    
    #세로 경계값
    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height
        
    #충돌처리를위한 정보
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    enemy_rect=enemy.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running=False


    screen.blit(background,(0,0)) #배경 그리기

    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    #타이머 넣기
    #경과 시간 게산
    elasped_time=(pygame.time.get_ticks()-start_ticks)/1000

    timer=game_font.render(str(int(total_time-elasped_time)),True,(255,255,255))

    screen.blit(timer,(10,10))

    #시간이 0이하이면 게임종료
    if total_time-elasped_time<=0:
        print("타임아웃")
        running=False

    pygame.display.update() #게임 화면을 다시 그리기

pygame.time.delay(2000)

#pygame 종료
pygame.quit()
