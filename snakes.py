import pygame
import random

#music
pygame.mixer.init()
pygame.mixer.music.load('music/wc.mp3')
pygame.init()

width=800
height=600
#gamewindow
gamewindow=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")


#background
bgimg=pygame.image.load("background/start.jpg")
bgimg=pygame.transform.scale(bgimg,[width,height]).convert_alpha()

#colours
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)
aqua=(0,255,255)
deepskyblue=(0,191,255)
gray=(255,215,0)
greenyellow=(173,255,47)
indigo= (75,0,130)
indianred=(255,106,106)
magenta=(255,0,255)
yellow=(255,255,0)
orange=(255,128,0)
violet=(238,130,238)
#-------------------------------------------------------
clock=pygame.time.Clock()
font_=pygame.font.SysFont('calibri',38,True)
#scoreboard
def screentext(text,color,x,y):
    screen_text=font_.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
def snake_body(screen,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(screen,color,[x,y,snake_size,snake_size])  
def welcome():
    bgimg=pygame.image.load("background/start.jpg")
    bgimg=pygame.transform.scale(bgimg,[width,height]).convert_alpha()
    gamewindow.blit(bgimg,[0,0])
    exit_game=False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(bgimg,(0,0))
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                exit_game=True
                pygame.quit()
                quit()
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_SPACE):
                    pygame.mixer.music.load('music/landscape.mp3')
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.2)
                    bgimg=pygame.image.load("background/bg2.jpg")
                    bgimg=pygame.transform.scale(bgimg,[width,height]).convert_alpha()
                    gamewindow.blit(bgimg,[0,0])
                    gameloop()
        pygame.display.update()
        clock.tick(30)
#game loop
def gameloop():
    with open("highscore.txt","r") as f:
        HIGHSCORE=int(f.read())
    #game specifications
    exit_game=False
    game_over=False
    bar_dist=43
    position_x=random.randint(0,width)
    position_y=random.randint(45,height)
    food_x=random.randint(10,width-10)
    food_y=random.randint(46,height-10)
    food_size=9
    vel_int=6
    velocity_x=vel_int
    velocity_y=vel_int
    snake_size=10
    fps=30
    score=0
    snake_length=1
    snake_list=[]
    fact=0
    #----------------------------------------------------------
    while not exit_game:
        if (game_over==True):
            pygame.time.delay(100)
            with open("highscore.txt","w") as f:
                f.write(str(HIGHSCORE))
            gamewindow.fill(greenyellow)
            bgimg=pygame.image.load("background/bg.jpg")
            bgimg=pygame.transform.scale(bgimg,[width,height]).convert_alpha()
            gamewindow.blit(bgimg,[0,0])
            screentext("GAME OVER !",black,300,250)
            screentext("Press ENTER to continue",indianred,225,325)
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    exit_game=True
                if(event.type==pygame.KEYDOWN):
                    if(event.key==pygame.K_RETURN):
                        pygame.mixer.music.load('music/wc.mp3')
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(0.2)
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT :
                    exit_game=True
                elif(event.type==pygame.KEYDOWN):
                    if event.key == pygame.K_RIGHT:
                        fact=1
                    elif event.key == pygame.K_LEFT:
                        fact=2
                    elif event.key == pygame.K_UP:
                        fact=3
                    elif event.key == pygame.K_DOWN:
                        fact=4
                    pygame.display.update()
            if(fact==1):
                position_x+=velocity_x
                if(position_x>width-snake_size):
                    position_x=snake_size
            elif(fact==2):
                position_x-=velocity_x
                if(position_x<0):
                    position_x=width-snake_size
            elif(fact==3):
                position_y-=velocity_y
                if(position_y<bar_dist):
                    position_y=height-snake_size
            elif(fact==4):
                position_y+=velocity_y
                if(position_y>height-snake_size):
                    position_y=bar_dist
            #checking for eating of food        
            if(abs(position_x-food_x)<snake_size+4 and abs(position_y-food_y)<snake_size+4):
                food_x=random.randint(10,width-10)
                food_y=random.randint(46,height-10)
                snake_length+=3
                score+=10
                if (score>HIGHSCORE):
                    HIGHSCORE=score
                #increasing speed
                if(score!=0 and (score)%50==0):
                    velocity_x+=vel_int*0.02
                    velocity_y+=vel_int*0.02

            #creating game screen    
            gamewindow.fill(greenyellow)
            bgimg=pygame.image.load("background/bg2.jpg")
            bgimg=pygame.transform.scale(bgimg,[width,height]).convert_alpha()
            gamewindow.blit(bgimg,[0,0])
            pygame.draw.line(gamewindow,white,[0,40],[width,40],3)
            #----------------------------------------------------------------------
            #SNAKE CREATION 
            head=[]
            head.append(position_x)
            head.append(position_y)
            snake_list.append(head)
            if(len(snake_list)>snake_length):
                del snake_list[0]
            snake_body(gamewindow,red,snake_list,snake_size)
            #-----------------------------------------------------------------------
            #CREATING FOOD 
            pygame.draw.circle(gamewindow,yellow,[food_x,food_y],food_size,0)
            #scoreboard updating
            screentext("SCORE : " +str(score),orange,5,7)
            screentext("HIGHSCORE : " + str(HIGHSCORE),greenyellow,515,7)
            #collision
            if head in snake_list[:-1]:
                    game_over=True
                    pygame.mixer.music.load('music/Big Explosion Cut Off.mp3')
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.5)
        clock.tick(fps)
        pygame.display.update()

    #loop end    
    pygame.quit()
    quit()
#calling gameloop
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)    
welcome()
