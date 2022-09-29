import pygame as pg

#initialize the pygames
pg.init()

#create the screen
screen = pg.display.set_mode((800,600))

#title and icon
pg.display.set_caption("Space Invaders")
icon = pg.image.load('assets/spaceship.png')
pg.display.set_icon(icon)

#game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
    
    screen.fill((0,0,0))
    pg.display.update()