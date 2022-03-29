import pygame
import math
import random

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("My Game of Space")
icon=pygame.image.load('./images/ufo.png')
pygame.display.set_icon(icon)
background=pygame.image.load('./images/background.png')
pygame.mixer.music.load('./images/background.wav')
pygame.mixer.music.play(-1)

playerimg=pygame.image.load('./images/player.png')
playerX=370
playerY=480
player_change=0

enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6


for i in range (num_of_enemies):
    enemyimg.append(pygame.image.load('./images/enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

pygame.mixer.init()
laser_sound = pygame.mixer.Sound('./images/laser.wav')
explosion_sound = pygame.mixer.Sound('./images/explosion.wav')

'''enemyimg=pygame.image.load('enemy.png')
enemyX=370
enemyY=50
enemy_change=5'''

bulletimg = pygame.image.load('./images/bullet.png')
bulletX = 0
bulletY = 480
bullet_changeX = 0
bullet_changeY = 10
bullet_state = 'ready'

font=pygame.font.Font('freesansbold.ttf',64)
score_value = 0

textX = 10
textY = 10

over_font=pygame.font.Font('freesansbold.ttf',64)


def show_score(x, y):


    score = font.render("Score :  " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))


def game_over_text():
    over_text=over_font.render("Game Over", True, (255,255,255))
    screen.blit(over_text, (200,250))


def player(x,y):
    screen.blit(playerimg,(x,y))
    '''blits means draw'''

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global  bullet_state
    bullet_state='fire'
    screen.blit(bulletimg,(x+16,y+10))

def iscollision(eneymX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(eneymX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return  False

spaceimage=pygame.image


running=True
while running:
    '''screen.fill(r,g,b)'''
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_change=-5
            elif event.key==pygame.K_RIGHT:
                player_change=5
            elif event.key==pygame.K_SPACE:
                laser_sound.play()
                bulletX=playerX
                fire_bullet(bulletX,bulletY)

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                player_change=0
    if playerX<=0:
        playerX=0
    if playerX>=736:
        playerX=736

    playerX=playerX+player_change

    for i in range (num_of_enemies):
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i]=4
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-4
            enemyY[i]+=enemyY_change[i]

        collission = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collission:
            explosion_sound.play()

            bullet_state = 'ready'
            bulletY = 480
            score_value += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i]= random.randint(50,150)
        enemy(enemyX[i], enemyY[i], i)



 
    if bulletY <= 0:
        bulletY= 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(playerX,bulletY)
        bulletY -= bullet_changeY




    player(playerX,playerY)
    show_score(textX, textY)
    pygame.display.update()
