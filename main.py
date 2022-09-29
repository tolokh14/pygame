import pygame as pg

#initialize the pygames
pg.init()

#create the screen
screen = pg.display.set_mode((800,600))

#title and icon
pg.display.set_caption("Space Invaders")
icon = pg.image.load('assets/spaceship.png')
pg.display.set_icon(icon)

#player
playerImg = pg.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

#game loop
running = True
while running:
    
    screen.fill((0,0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

        #check keyboard press
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerX_change = -0.3
            if event.key == pg.K_RIGHT:
                playerX_change = 0.3
            if event.key == pg.K_UP:
                playerY_change = -0.3
            if event.key == pg.K_DOWN:
                playerY_change = 0.3
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerX_change = 0
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    player(playerX,playerY)
    pg.display.update()