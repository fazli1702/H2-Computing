import pygame as pg
import random

#initialise
pg.init()

#screen
screen = pg.display.set_mode((500, 500))
pg.display.set_caption('Snake')
x = 900
y = 900


#colour
##black = (0, 0, 0)
##white = (255, 255, 255)
##red = (255, 0, 0)
##green = (0, 255, 0)



#main while loop

run = True

while run:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

pg.quit()
