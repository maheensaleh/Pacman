import pygame
import time
pygame.init()
pygame.mixer.init()
#colors
white=(255,255,255)
red=(255,0,0)
yellow=(255,255,0)
black=(0,0,0)
lime=(0,255,0)
blue=(0,0,205)
coral=(255,0,196)
l_violet=(255,127,0)
l_green=(127,255,0)
lives=3
highsc=0
#window
window_width=800
window_height=600
gamewindow=pygame.display.set_mode((window_width,window_height+50))
pygame.display.set_caption('Pacman')
fps=pygame.time.Clock()

#images:
b_g=pygame.image.load('b_g.png')
r_g=pygame.image.load('r_g.png')
p_g=pygame.image.load('p_g.png')
o_g=pygame.image.load('o_g.png')
p_l=pygame.image.load('pl.png')
p_d=pygame.image.load('pd.png')
p_u=pygame.image.load('pu.png')
cherry=pygame.image.load('mycherry.png')
orange=pygame.image.load('ora.png')
stb=pygame.image.load('str.png')
#starting music:
#pacsc=pygame.mixer.music.load('pacman_music.wav')

def mess(message,color,size,x,y):
    text_type=pygame.font.SysFont(None, size)
    test_disp=text_type.render(message,True,color)
    gamewindow.blit(test_disp,(x,y))

def high_s(count):
    global highsc
    if count>highsc:
        highsc=count

def lives_func():
    global lives
    lives-=1
    if lives!=0:
        gameloop() 
        gameover==False
    elif lives==0:
        lives=3
        #mess('out',red,90,300,250)
        #pygame.display.update()
        time.sleep(1)
        gameloop()

def yay(x):
    font=pygame.font.SysFont('algerian',100)
    text=font.render('GREAT!+5',True,l_violet)
    all_fonts=pygame.font.get_fonts()
    gamewindow.blit(text,(100,220))
    pygame.mixer.music.load('fruit_music.wav')
    pygame.mixer.music.play(2, 0)
    #pygame.mixer.music.fadeout(3000)
    pygame.display.update()
    time.sleep(2.5)
    pygame.mixer.music.load('Pacman_music.wav')
    pygame.mixer.music.play(-1, 0)

def work():
    menu = True
    while menu == True:
        gamewindow.fill(black)
        pcpic = pygame.image.load('pcpic2.png')
        pl_use = pygame.image.load('pl_use.png')
        qt_use = pygame.image.load('quit.png')
        gamewindow.blit(pcpic, (0, 0))
        gamewindow.blit(pl_use, (380, 350))
        gamewindow.blit(qt_use, (380, 400))
        mess('Credits:',white,50,550,450)
        mess('Maheen Saleh',white,50,550,500)
        mess('Sara Fatima', white, 50, 550, 550)
        mess('Ali Abbas', white, 50, 550, 600)
        pygame.display.update()
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                pygame.quit()
                quit()
            if x.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 380 <= mx < 470 and 350 <= my <= 390:
                    menu = False
                if 385 <= mx <= 480 and 410 <= my <= 423:
                    time.sleep(0.3)
                    menu = False
                    pygame.quit()
                    quit()


def gameloop():
    #exit=False
    gameover=False
    gamewin=False
    #menu=True
    #pacman :
    eatengoal=[]
    food = []
    manx=400
    many=0
    c_manx=0
    c_many=0
    pv=20
    gv=20
    score=-1
    pacman=pygame.image.load('pr.png')
    pygame.mixer.music.load('pacman_music.wav')
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1,0.0)
    n=0
    ##ghosts:
    g1x=0
    g1y=0
    g2x=60
    g2y=60
    g3x=120
    g3y=120
    g4x=180
    g4y=180
    g5x=240
    g5y=240
    #fruits
    mycherryx=0
    mycherryy=20
    stbx=60
    stby=80
    orx=200
    ory=120

    while True:
        if (lives == 3 or lives == 0) and n == 0:
            n += 1
            work()
        while gamewin==True:
            mess('YOU WIN',lime,200,100,200)
            pygame.display.update()
            time.sleep(3)
            gamewin=False
            gameloop()


        while gameover==True:
            gamewindow.fill(black)
            gameover_pic = pygame.image.load('over.png')
            quit_button=pygame.image.load('quit.png')
            restart_button=pygame.image.load('restart.png')
            gamewindow.blit(gameover_pic, (0, 0))
            gamewindow.blit(quit_button,(350,550))
            gamewindow.blit(restart_button,(350,480))
            mess('high score:'+str(highsc),red,50,300,600)
            mess('lives:' + str(lives-1), red, 50, 50, 510)
            mess('score ' + str(score), red, 50, 580, 510)
            pygame.display.update()

            for  x in pygame.event.get():
                if x.type==pygame.QUIT:
                    #exit=True
                    pygame.quit()
                    quit()
                if x.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    print(mx,my)
                    if 360<=mx<=450 and 485<=my<=515:
                        lives_func()
                        gameover==False
                    elif 365<=mx<=440 and 560<=my<=590:
                        #exit=True
                        pygame.quit()
                        quit()
         #to give bakground colour
        gamewindow.fill(black)
        ##rectangel 1:
        pygame.draw.rect(gamewindow,blue,[40,40,18,500])
        pygame.draw.rect(gamewindow,blue,[40,40,700,18])
        pygame.draw.rect(gamewindow,blue,[740,40,20,500])
        pygame.draw.rect(gamewindow,blue,[40,540,720,20])
        ##rectangle 2;
        pygame.draw.rect(gamewindow,blue,[100,100,18,400])
        pygame.draw.rect(gamewindow,blue,[100,100,600,18])
        pygame.draw.rect(gamewindow,blue,[680,100,20,400])     
        pygame.draw.rect(gamewindow,blue,[100,480,600,20])
        ##rectangle 3;
        pygame.draw.rect(gamewindow,blue,[160,160,18,280])
        pygame.draw.rect(gamewindow,blue,[160,160,480,18])
        pygame.draw.rect(gamewindow,blue,[620,160,20,280])
        pygame.draw.rect(gamewindow,blue,[160,420,480,20])
        ##rectangle 4:
        pygame.draw.rect(gamewindow,blue,[220,220,18,140])
        pygame.draw.rect(gamewindow,blue,[220,220,340,18])
        pygame.draw.rect(gamewindow,blue,[540,220,20,160])
        pygame.draw.rect(gamewindow,blue,[220,360,340,20])

        pygame.draw.rect(gamewindow,yellow,[0,600,window_width,20])

        #to draw goals:
        goalx=10
        goaly=10
        while goaly<=window_height:
            goalx=10
            while goalx<window_width:
                goal_c=gamewindow.get_at_mapped((goalx,goaly))
                if (goalx,goaly) not in eatengoal and goal_c!=205 :
                    pygame.draw.circle(gamewindow,coral,(goalx,goaly),5)
                goalx+=20
            goaly+=20

        #gamer overs when character touches the ghost
        if manx>=g1x-40 and manx<=g1x+40:
            if many>=g1y-40 and many<=g1y+40:
                if manx<=40 or manx >=760 or many<=40 or many>=560:
                    gameover=True
                    pygame.mixer.music.load('pacman_death.wav')
                    pygame.mixer.music.play(1,0)
                    pygame.mixer.music.fadeout(2000)
        elif manx>=g2x-40 and manx<=g2x+40:
            if many>=g2y-40 and many<=g2y+40:
                if 60<=manx<=100 or 700<=manx<=740 or 60<=many<=100 or 500<=many<=540:
                    gameover=True
                    pygame.mixer.music.load('pacman_death.wav')
                    pygame.mixer.music.play(1,0)
                    pygame.mixer.music.fadeout(2000)
        elif manx>=g3x-40 and manx<=g3x+40:
            if many>=g3y-40 and many<=g3y+40:
                #if 120<=manx<=160 or 640<=manx<=680 or 120<=many<=160 or 440<=many<=480:
                    gameover=True
                    pygame.mixer.music.load('pacman_death.wav')
                    pygame.mixer.music.play(1,0)
                    pygame.mixer.music.fadeout(2000)
        elif manx>=g4x-40 and manx<=g4x+40:
            if many>=g4y-40 and many<=g4y+40:
                #if 180<=manx<=220 or 580<=manx<=620 or 180<=many<=220 or 380<=many<=420:
                    gameover=True
                    pygame.mixer.music.load('pacman_death.wav')
                    pygame.mixer.music.play(1,0)
                    pygame.mixer.music.fadeout(2000)
        elif manx>=g5x-40 and manx<=g5x+40:
            if many>=g5y-40 and many<=g5y+40:
                    gameover=True
                    pygame.mixer.music.load('pacman_death.wav')
                    pygame.mixer.music.play(1,0)
                    pygame.mixer.music.fadeout(2000)
        ## rectangle doors:
        if len(eatengoal)>=264:
            pygame.draw.rect(gamewindow,lime,[740, 250, 20, 50])
        if len(eatengoal)>=481:
            pygame.draw.rect(gamewindow,lime,[100, 250, 18, 50])
        if len(eatengoal)>=650:
            pygame.draw.rect(gamewindow,lime,[300, 420, 50, 20])
        if len(eatengoal)>=771:
            pygame.draw.rect(gamewindow,lime,[390, 220, 50, 18])

        #titlebar
        mess('lives:'+str(lives), white, 50, 0, 620)
        mess('score ' + str(score), white, 50, 580, 620)

        ##this for loopis to take inputs for game;
        for x in pygame.event.get():
            # this condition is toclose game when quit is selected
            if x.type==pygame.QUIT:
               # exit=True
                pygame.quit()
                quit()
            # to act upon arrow keys

            if x.type==pygame.KEYDOWN:
                if x.key==pygame.K_RIGHT:
                    pacman=pygame.image.load('pr.png')
                    c_manx=gv
                    c_many=0
                elif x.key==pygame.K_LEFT:
                    pacman=pygame.image.load('pl.png')
                    c_manx=-gv
                    c_many=0
                elif x.key==pygame.K_UP  :
                    pacman=pygame.image.load('pu.png')
                    c_many=-gv
                    c_manx=0
                elif x.key==pygame.K_DOWN  :
                    pacman=pygame.image.load('pd.png')
                    c_many=gv
                    c_manx=0
                #elif x.key==pygame.K_SPACE:
                 #   gameloop()
        manx+=c_manx
        many+=c_many
        ###to give corner boundaries
        if manx>window_width-20 or manx<20 or many>window_height-20 or many<20:
            if manx>window_width-20 :
                manx=0
            elif manx<0:
                manx=window_width-20
            elif many>window_height-20:
                many=0
            elif many<0:
                many=window_height-20
            #colour2=gamewindow.get_at_mapped((manx,many))
            gamewindow.blit(pacman,(manx,many))
                
        else:
            ##to give boundary of box
            colour=gamewindow.get_at_mapped((manx,many))
            if colour!=205 :
                #colour2=gamewindow.get_at_mapped((manx,many))
                gamewindow.blit(pacman,(manx,many))
            else:
                manx-=c_manx
                many-=c_many
                #colour2=gamewindow.get_at_mapped((manx,many))
                gamewindow.blit(pacman,(manx,many))

        #ghost display and movements
        if g1y==0:
            if g1x<=760:
                gamewindow.blit(b_g,(g1x,g1y))
                g1x+=gv
        if g1x==760:
            if g1y<=560:
                gamewindow.blit(b_g,(g1x,g1y))
                g1y+=gv
        if g1y==560:
            if g1x>=0:
                gamewindow.blit(b_g,(g1x,g1y))
                g1x+=-gv
        if g1x==0:
            if g1y>=0:
                gamewindow.blit(b_g,(g1x,g1y))
                g1y+=-gv
        #ghost2
        if g2y==60:
            if g2x<=700:
                gamewindow.blit(r_g,(g2x,g2y))
                g2x+=20
        if g2x==700:
            if g2y<=500:
                gamewindow.blit(r_g,(g2x,g2y))
                g2y+=20
        if g2y==500:
            if g2x>=60:
                gamewindow.blit(r_g,(g2x,g2y))
                g2x+=-20
        if g2x==60:
            if g2y>=60:
                gamewindow.blit(r_g,(g2x,g2y))
                g2y+=-20
        #ghost3
        if g3y==120:
            if g3x<=640:
                gamewindow.blit(p_g,(g3x,g3y))
                g3x+=20
        if g3x==640:
            if g3y<=440:
                gamewindow.blit(p_g,(g3x,g3y))
                g3y+=20
        if g3y==440:
            if g3x>=120:
                gamewindow.blit(p_g,(g3x,g3y))
                g3x+=-20
        if g3x==120:
            if g3y>=120:
                gamewindow.blit(p_g,(g3x,g3y))
                g3y+=-20
        #ghost4
        if g4y==180:
            if g4x<=580:
                gamewindow.blit(o_g,(g4x,g4y))
                g4x+=20
        if g4x==580:
            if g4y<=380:
                gamewindow.blit(o_g,(g4x,g4y))
                g4y+=20
        if g4y==380: 
            if g4x>=180:
                gamewindow.blit(o_g,(g4x,g4y))
                g4x+=-20
        if g4x==180:
            if g4y>=180:
                gamewindow.blit(o_g,(g4x,g4y))
                g4y+=-20

        #food appearing
        if mycherryx not in food:
            cherry=pygame.image.load('mycherry.png')
            gamewindow.blit(cherry,(mycherryx,mycherryy))
        if stbx not in food:
            stb=pygame.image.load('str.png')
            gamewindow.blit(stb,(stbx,stby))
        if orx not in food:
            orange=pygame.image.load('ora.png')
            gamewindow.blit(orange,(orx,ory))
             
        ##saving the eaten goals:
        if (manx+10,many+10) not in eatengoal:
            eatengoal.append((manx+10,many+10))
            score += 1
            high_s(score)
        #saving eaten fruits :
        if mycherryx==manx and mycherryy==many or(stbx==manx and stby==many) or (orx==manx and ory==many):
            eatengoal.append((manx,many))
            if (manx,many) in eatengoal:
                score+=5
                food.append(manx)
                yay(5)
        #giving score and highscore

        #gamewin:
        if len(eatengoal)>=867:
            gamewin=True
        pygame.display.update()
        fps.tick(8)
gameloop()