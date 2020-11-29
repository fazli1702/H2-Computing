#Animation is simply using a For-loop
# to do the following repeatedly:
#1. clearing screen
#2. drawing all your objects
#3. displaying 


###### LESSON 3 ######
#In this lesson, we will animate the movement of 2 rectangles,
#using a For-loop, with delay set at 1/40th of a second.


import pygame
import math

#define size of graphics display
DISPLAY=(400,300)

#initialise the pygame game clock
clock = pygame.time.Clock()

#initialise pygame and display
pygame.init()
screen = pygame.display.set_mode(DISPLAY)

#fill background with blue colour first 
screen.fill((30, 100, 160))

#Display objects blitted into memory
pygame.display.flip()

for x in range(10,250):
    #a. clear: fill the background to empty it
    screen.fill((30, 100, 160))

    #b. draw:
    #Rectangle 1 at a location (x,100) with width 50 ht 20
    pygame.draw.rect(screen,(255,255,255), pygame.Rect(x, 100, 50, 20))
    #Rectangle 2 at a location (x,200) with width 50 ht 20, with varying colour
    pygame.draw.rect(screen,(x,0,0), pygame.Rect(x, 200, 50, 20))
    
    #c. display: flip the page, to display it
    pygame.display.flip()

    #d. Control Framerate : delay 1/40th of a second every loop, to slow down, to see the animation
    clock.tick(40)


