import pygame as pg
import random as ran
import math
from pygame import mixer as mix

# initialize the pygames
pg.init()

# create the screen
screen = pg.display.set_mode((800, 600))

# background
background = pg.image.load('assets/background.png')

# background music
mix.music.load('assets/background.wav')
mix.music.play(-1)

#title and icon
pg.display.set_caption("Space Invaders")
icon = pg.image.load('assets/spaceship.png')
pg.display.set_icon(icon)

# player
playerImg = pg.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range (num_of_enemies):
    enemyImg.append(pg.image.load('assets/alien.png'))
    enemyX.append(ran.randint(0, 735))
    enemyY.append(ran.randint(0,40))
    enemyX_change.append(ran.randint(4,8))
    enemyY_change.append(40)

# bullet
bulletImg = pg.image.load('assets/bullet.png')
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#score
score_value = 0
font = pg.font.Font('assets/Minecrafter.Reg.ttf',32)

textX = 10
textY = 10

#game over text
over_font = pg.font.Font('assets/Minecrafter.Reg.ttf',64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(250,250))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision (enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# game loop
running = True
while running:

    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

        # check keyboard press
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerX_change = -5
            if event.key == pg.K_RIGHT:
                playerX_change = 5
            if event.key == pg.K_UP:
                playerY_change = -5
            if event.key == pg.K_DOWN:
                playerY_change = 5
            if event.key == pg.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mix.Sound('assets/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX,bulletY)

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerX_change = 0
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    # check the boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # enemy movement
    for i in range(num_of_enemies):
#(enemyY[i] >= playerY-50 and enemyX[i] >= playerX-50)
#(enemyY[i] >= playerY-50 and enemyX[i] <= playerX+50)
        #game over
        # if  (enemyY[i] >= playerY-50 and enemyX[i] <= playerX+50):
        #     print('hit')

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        
        #collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound = mix.Sound('assets/explosion.wav')
            explosion_sound.play()
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = ran.randint(0, 735)
            enemyY[i] = 40
        
        enemy(enemyX[i], enemyY[i],i)
    
    #bullet movement
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX,textY)
    pg.display.update()
