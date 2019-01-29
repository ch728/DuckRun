import pygame
import pygame.mixer
import classes.block as bg
import classes.duck as duck
import classes.rock as rock
import classes.item as item
import classes.super as sup
import classes.explosion as explosion
from itertools import cycle
import random


def main():
    pygame.mixer.pre_init(44100, -16, 2, 1024)
    pygame.init()
    pygame.mixer.init()

    # load cursor
    pygame.mouse.set_cursor((16, 19), (0, 0),
                            (128, 0, 192, 0, 160, 0, 144, 0, 136, 0, 132,
                            0, 130, 0, 129, 0, 128, 128, 128, 64, 128, 32,
                            128, 16, 129, 240, 137, 0, 148, 128, 164, 128, 194,
                            64, 2, 64, 1, 128), (128, 0, 192, 0, 224, 0, 240,
                            0, 248, 0, 252, 0, 254, 0, 255, 0, 255, 128, 255,
                            192, 255, 224, 255, 240, 255, 240, 255, 0, 247,
                            128, 231, 128, 195, 192, 3, 192, 1, 128))

    # define colors
    blue = (15, 131, 246)
    black = (0, 0, 0)
    white = (250, 250, 250)

    # define fonts
    textf = pygame.font.SysFont("Bitstream Vera Sans", 30)
    texts = pygame.font.SysFont("Bitstream Vera Sans", 20)

    # make playlists
    scenes = [r'sound/Intro_dance.ogg', r"sound/direction_theme.ogg",
              r"sound/game_over.ogg"]
    duck_songs = [r'sound/main_theme_red_duck.ogg',
                  r'sound/main_theme_yellow_duck.ogg',
                  r'sound/ain_theme_pink_duck.ogg']

    #make a picture albums
    back_pics=[r"pics/intro.png",r"pics/game_over.png"]
    duck_pics=[r"pics/red_duck.png",r"pics/yellow_duck.png",r"pics/pink_duck.png"]
    text_pics=[r"pics/title.png",r"pics/up_key.png",r"pics/down_key.png",
               r"pics/up_key_blank.png",r"pics/down_key_blank.png"]
    enemy_pics=[r"pics/rock.png"]
    item_pics=[r"pics/bread_crumb.png",r"pics/heart.png",r"pics/duck_token.png"]
    super_pics=[]
    for x in range(1,11,1):
        super_pics.append(r"pics/super_" + "%i.png"%x)
    exp_pics=[]
    for x in range(9):
        exp_pics.append(r"pics/regularExplosion0" +"%i.png"%x)

    #load sound effects
    super_sound=pygame.mixer.Sound(r"sound/super.ogg")
    squeak=pygame.mixer.Sound(r"sound/squeak.wav")
    quack=pygame.mixer.Sound(r"sound/quack.wav")


    #set up screen
    screen=pygame.display.set_mode((600,400))
    pygame.display.set_caption('Duck Run')

    # set clock t manage how fast the screen updates
    clock=pygame.time.Clock()
    #make a BLINKEVENT
    BLINK_EVENT = pygame.USEREVENT + 0
    #intialize an indicator variable that = True when player quits the game
    done=False

# =============================================================================
# Intro dance loop
# =============================================================================
    back=bg.Block(back_pics[0],(0,0))
    title=bg.Block(text_pics[0],(175,25))
    duck1=bg.Block(duck_pics[0],(50,450))
    duck2=bg.Block(duck_pics[1],(230,450))
    duck3=bg.Block(duck_pics[2],(550,450))


    pygame.mixer.music.load(scenes[0])
    pygame.mixer.music.play(-1)

    pos=450
    while not done and pos >150:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        screen.blit(back.image, back.rect)
        screen.blit(title.image,title.get_pos())
        screen.blit(duck1.image,duck1.rect)
        screen.blit(duck2.image,duck2.rect)
        screen.blit(duck3.image,duck3.rect)
        duck1.update(1,-5)
        duck2.update(0,-4)
        duck3.update(-4,-5)
        if pos%25==0:
            duck2.image=pygame.transform.flip(duck2.image, True, False)#makes the duck dance
            duck1.image=pygame.transform.flip(duck1.image, True, False)
            duck3.image=pygame.transform.flip(duck3.image, True, False)
        pygame.display.flip()
        pos+=-5
        clock.tick(5) #5 fps

# =============================================================================
# Pick a Duck loop
# =============================================================================
    choosing=True #used to indicate when a duck has been choosen
    pick=1 #

    #Setup for flashing "Click A Duck"
    clk=textf.render(" Click a Duck", False,black)
    blank=textf.render("Click a Duck",False,white)
    blinks=cycle([clk, blank]) #make an iterator to go between text and blank
    blink=next(blinks) #iterate
    pygame.time.set_timer(BLINK_EVENT,1000)

    while not done and choosing: #if duck is choosen or play quits, stop
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN or event.type== pygame.MOUSEBUTTONUP:#check if the cursor was clicked over a duck
                cursor_pos=pygame.mouse.get_pos()
                if (cursor_pos[0] >= duck1.rect[0] and cursor_pos[0] <=duck1.rect[0]+duck1.rect[2]) and (cursor_pos[1] >= duck1.rect[1] and cursor_pos[1] <=duck1.rect[1]+duck1.rect[3]):
                    quack.play()
                    pick=0
                    choosing=False
                elif (cursor_pos[0] >= duck2.rect[0] and cursor_pos[0] <=duck2.rect[0]+duck2.rect[2]) and (cursor_pos[1] >= duck2.rect[1] and cursor_pos[1] <=duck2.rect[1]+duck2.rect[3]):
                    quack.play()
                    pick=1
                    choosing=False
                elif (cursor_pos[0] >= duck3.rect[0] and cursor_pos[0] <=duck3.rect[0]+duck3.rect[2]) and (cursor_pos[1] >= duck3.rect[1] and cursor_pos[1] <=duck3.rect[1]+duck3.rect[3]):
                    quack.play()
                    pick=2
                    choosing=False
            elif  event.type == BLINK_EVENT:
                blink=next(blinks)
            elif event.type == pygame.QUIT:
                done=True
        screen.blit(back.image, back.get_pos())
        screen.blit(title.image,title.get_pos())
        screen.blit(duck1.image,duck1.get_pos())
        screen.blit(duck2.image,duck2.get_pos())
        screen.blit(duck3.image,duck3.get_pos())
        screen.blit(blink,(250,300))
        duck2.image=pygame.transform.flip(duck2.image, True, False)
        duck1.image=pygame.transform.flip(duck1.image, True, False)
        duck3.image=pygame.transform.flip(duck3.image, True, False)
        pygame.display.flip()
        clock.tick(1)
    pygame.mixer.music.stop()

# =============================================================================
# Direction Screen Loop
# =============================================================================
    main_duck=bg.Block(duck_pics[pick],(150,250))
    rock1=bg.Block(enemy_pics[0],(600,150))
    rock2=bg.Block(enemy_pics[0],(550,325))
    rock3=bg.Block(enemy_pics[0],(550,200))
    crumb=bg.Block(item_pics[0],(550,275))
    down_key=bg.Block(text_pics[1],(50,175))
    down_blank=bg.Block(text_pics[3],(50,175))

    up_key=bg.Block(text_pics[2],(50,225))
    up_blank=bg.Block(text_pics[4],(50,225))

    line1= textf.render("Swim courageously", False, black)
    line2=textf.render("Dodge, feed, dodge, and prevail", False, black)
    line3=textf.render("Swiftly, duck, swiftly", False, black)

    #setup for flashing text
    clk=textf.render("Press any Key to Continue",False, black)
    blank=textf.render("Press any Key to Continue",False, white)
    blinks=cycle([clk, blank]) #make an iterator to go between text and blank
    blink=next(blinks) #iterate

    #setup for flashing buttons
    up_blks=cycle([down_key,down_blank])
    down_blks=cycle([up_key,up_blank])
    up_blk=next(up_blks)
    down_blk=next(down_blks)



    pygame.time.set_timer(BLINK_EVENT,400)

    pygame.mixer.music.load(scenes[1])
    pygame.mixer.music.play(-1)

    up=1
    clicked = False
    counter=0
    score=texts.render("Score: %i"%counter,False,white)
    while not done and not clicked:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            elif event.type == pygame.KEYDOWN :
                clicked=True
            elif event.type==BLINK_EVENT:
                 blink=next(blinks)
                 up_blk=next(up_blks)
                 down_blk=next(down_blks)
         screen.fill(blue)
         screen.blit(score,(5,10))
         screen.blit(line1,(175,25))
         screen.blit(line2,(125,60))
         screen.blit(line3,(175,95))
         screen.blit(blink,(150,350))
         screen.blit(rock1.image,rock1.get_pos())
         screen.blit(rock2.image,rock2.get_pos())
         screen.blit(rock3.image,rock3.get_pos())
         screen.blit(crumb.image,crumb.get_pos())
         rock1.update(-2,0)
         rock2.update(-1,0)
         rock3.update(-3,0)
         crumb.update(-3,0)
         if crumb.rect.colliderect(main_duck.rect):
             crumb.kill()
             quack.play()
             counter+=1
             score=texts.render("Score: %i"%counter,False,white)
             crumb=bg.Block(item_pics[0],(550,275))
         duck_pos=main_duck.get_pos()

         if duck_pos[1]+ duck_pos[3] == 170:
             if rock1.get_pos()[0] <0:
                 rock1.update(-1*rock1.get_pos()[0]+600,0)
             if rock3.get_pos()[0] <0:
                 rock3.update(-1*rock3.get_pos()[0]+600,0)
             if crumb.get_pos()[0] <0:
                 crumb.update(-1*crumb.get_pos()[0]+600,0)
             up=0
         if duck_pos[1]==300:
             if rock2.get_pos()[0] <0:
                 rock2.update(-1*rock2.get_pos()[0]+600,0)
             up=1
         if up:
             main_duck.update(0,-1)
             screen.blit(up_blk.image,up_blk.get_pos())
             screen.blit(up_key.image,up_key.get_pos())
             screen.blit(main_duck.image,main_duck.get_pos())
         else:
            main_duck.update(0,1)
            screen.blit(down_blk.image,down_blk.get_pos())
            screen.blit(down_key.image,down_key.get_pos())
            screen.blit(main_duck.image,main_duck.get_pos())

         pygame.display.flip()
         clock.tick(90)
    pygame.mixer.music.stop()

# =============================================================================
# Main game loop
# =============================================================================
    player=duck.Duck(duck_pics[pick],(125,200))
    main_duck=pygame.sprite.Group()
    main_duck.add(player)

    heart1=bg.Block(item_pics[1],(250,15))
    heart2=bg.Block(item_pics[1],(280,15))
    heart3=bg.Block(item_pics[1],(310,15))

    enemies=pygame.sprite.Group()
    bread=pygame.sprite.Group()
    life=pygame.sprite.Group()
    super_token=pygame.sprite.Group()
    sup_sprite=pygame.sprite.Group()
    explode=pygame.sprite.Group()


    pygame.mixer.music.load(duck_songs[pick])
    pygame.mixer.music.play(-1)

    counter=0
    minutes=0
    frames=0
    total=3
    super_stat=0
    score=texts.render("Score: %i"%counter,False,white)
    while not done and player.get_health() >0:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if len(sup_sprite)==1:
                sup_sprite.update(-10)
            player.update(-1,super_stat)
        if keys[pygame.K_DOWN]:
             if len(sup_sprite)==1:
                sup_sprite.update(10)
             player.update(1,super_stat)
        if player.rect[1]+player.rect[3] >=405 or player.rect[1]+player.rect[1] <=-5:
            player.update_health(-3)

        frames+=1
        if frames == 60*60: #keep track of minutes
           frames=0
           minutes+=1
           total=1*minutes+total # allow one more enemy every minute

        num_enemies=len(enemies.sprites()) #spawn enemies
        if num_enemies < total:
            make=total-num_enemies
            for x in range(make):
                enemies.add(make_rocks(enemy_pics[0]))

        num_bread=len(bread.sprites()) #spawn bread
        if num_bread < total:
            make=total-num_bread
            for x in range(make):
                bread.add(make_item(item_pics[0],-3))

        if len(life) == 0 and random.uniform(0,1) > 0.999: #spawn heart containers
                life.add(make_item(item_pics[1],-3))

        if random.uniform(0,1) >0.999 and len(sup_sprite) ==0 and len(super_token)==0:
                super_token.add(make_item(item_pics[2],-6))

        screen.fill(blue)

        if player.get_health()==3:
            screen.blit(heart1.image,heart1.rect)
            screen.blit(heart2.image,heart2.rect)
            screen.blit(heart3.image,heart3.rect)
        elif player.get_health()==2:
            screen.blit(heart1.image,heart1.rect)
            screen.blit(heart2.image,heart2.rect)
        else:
            screen.blit(heart1.image,heart1.rect)

        screen.blit(score,(5,10))
        screen.blit(player.image,player.rect)

        sup_sprite.draw(screen)
        enemies.draw(screen)
        super_token.draw(screen)
        bread.draw(screen)
        life.draw(screen)
        explode.draw(screen)

        sup_sprite.update(0)
        enemies.update(super_stat)
        bread.update(super_stat)
        super_token.update(super_stat)
        life.update(super_stat)
        explode.update()

        pygame.display.flip()

        #check for sprite collisions
        hits=pygame.sprite.pygame.sprite.groupcollide(main_duck,enemies,False,True)
        if len(hits) >0:
            if super_stat !=1:
                player.update_health(-1)
                squeak.play()
            else:
                explode.add(explosion.Explosion(player.rect.center,exp_pics))


        catches=pygame.sprite.pygame.sprite.groupcollide(main_duck,bread,False,True)
        if len(catches) >0:
            counter+=1
            score=texts.render("Score: %i"%counter,False,white)
            quack.play()

        energy=pygame.sprite.pygame.sprite.groupcollide(main_duck,life,False,True)
        if len(energy) >0 and player.get_health() <3:
            player.update_health(1)
            quack.play()

        token=pygame.sprite.pygame.sprite.groupcollide(main_duck,super_token,False,True)
        if len(token) >0:
            sup_sprite.add(sup.Super(player.rect.center,super_pics))
            pygame.mixer.music.pause()
            pause_start=pygame.time.get_ticks()
            super_stat=1
            super_sound.play()

        now=pygame.time.get_ticks()

        if super_stat:
            if now - pause_start> 15*1000:
                pygame.mixer.music.unpause()
                super_stat=0

        clock.tick(60)

    if super_stat==1:
        super_sound.stop()
    pygame.mixer.music.stop()

    if done:
        pygame.quit()
        raise SystemExit
# =============================================================================
# Update high score file
# =============================================================================
    with open('high_score.txt', 'r') as f:
        high_score = f.readline().strip()
    if counter > int(high_score): #if previous high score is beat, update it
        with open('high_score.txt', 'w') as f:
            f.write(str(counter))
# =============================================================================
# Death Throes
# =============================================================================
    n=0
    flash=pygame.Surface((600,400))
    colors=cycle([black,white])
    color=next(colors)
    while n <5:
        squeak.play(1)
        n +=1
        flash.fill(color)
        screen.blit(flash,(0,0,600,400))
        color=next(colors)
        pygame.display.flip()
        clock.tick(2)


    game_over(back_pics,scenes,white,black,score,textf,texts) #game over function allows player to restart
# =============================================================================
# Functions
# =============================================================================
def game_over(back_pics,scenes,white,black,score,textf,texts):
    screen=pygame.display.set_mode((600,400))
    pygame.display.set_caption('Duck Run')

    over=bg.Block(back_pics[1],(0,0))
    with open('high_score.txt', 'r') as f:
        high_score = f.readline().strip()

    score2=texts.render("High score: %s"% high_score,False, white)

    clk=textf.render("Try Again",False, black)
    blank=textf.render("Try Again",False, white)
    blinks=cycle([clk, blank]) #make an iterator to go between text and blank
    blink=next(blinks) #iterate


    pygame.mixer.music.load(scenes[2])
    pygame.mixer.music.play(-1)

    clock=pygame.time.Clock()
    done=False
    button=False
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
                if event.type==pygame.MOUSEBUTTONDOWN or event.type== pygame.MOUSEBUTTONUP:#check if the cursor was clicked over a duck
                    cursor_pos=pygame.mouse.get_pos()
                    if (cursor_pos[0] >= 250 and cursor_pos[0] <=250+clk.get_width()) and (cursor_pos[1] >= 300 and cursor_pos[1] <=350+clk.get_height()):
                        button=True
        screen.blit(over.image,over.rect)
        screen.blit(score,(250,275))
        screen.blit(score2,(250,300))
        screen.blit(blink,(250,350))
        blink=next(blinks)
        pygame.display.flip()

        if button:
            main()
        clock.tick(2)

    pygame.mixer.music.stop()
    pygame.quit()
    raise SystemExit


def make_rocks(pic):
    tempy=random.randint(30,380)
    tempx=random.randint(700,1000)
    tempSpeed=-1*random.randint(2,4)
    size=random.uniform(0.7,1.5)
    return rock.Rock(pic,(tempx,tempy),tempSpeed,size)

def make_item(pic,speed):
    tempy=random.randint(30,380)
    tempx=random.randint(700,1000)
    return item.Item(pic,(tempx,tempy),speed)

if __name__ == '__main__':
   main()
