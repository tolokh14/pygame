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

def player():
    screen.blit(playerImg, (playerX, playerY))

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

    player()
    pg.display.update()