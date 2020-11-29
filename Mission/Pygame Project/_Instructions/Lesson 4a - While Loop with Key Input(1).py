#Implement a game loop using a While-Loop
#
#while True:
#   1. Check INPUT
#   2. PROCESS objects in game
#   3. Display/Refresh OUTPUT

#KEY INPUTS : 2 types of inputs to process:
#  1. One time events
#  2. Keys that are held down
#
# For detecting other possible input keys, use the Python IDLE shell:
# >>> import pygame
# >>> help(pygame)  

###### LESSON 4A ######
#In this lesson, we will implement a game loop,
#detecting key inputs and closing the game screen.
#
# Instructions:
# 1. Press left/right/up/down to move the rectangle
# 2. Press ESC key to close the game screen


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

#initialise game variables
xloc = 10
yloc = 100
done = False

#Game Loop
while done == False:

    ############
    # 1. INPUT #
    ############

    #>>>>>  1a. Process one time events  <<<<<
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xloc-=10
                print("User holds down left button")
            if event.key == pygame.K_RIGHT:
                xloc+=10
                print("User holds down right button")
            if event.key == pygame.K_UP:
                yloc-=10
                print("User pressed Up button")
            if event.key == pygame.K_DOWN:
                yloc+=10
                print("User pressed Down button")
            if event.key == pygame.K_ESCAPE:
                break

    #>>>>>  1b. Process keys that are held down  <<<<<
    pygame.event.get()
    pressed = pygame.key.get_pressed() 
    if pressed[pygame.K_LEFT]:
        xloc-=2
        #generally not a good idea to put print statements here
    if pressed[pygame.K_RIGHT]:
        xloc+=2
    if pressed[pygame.K_UP]:
        yloc-=2
    if pressed[pygame.K_DOWN]:
        yloc+=2
    if pressed[pygame.K_ESCAPE]:
        break


    #############
    # 2.PROCESS #
    #############

    xloc+=1  #moves the rectangle 1 pixel right each frame (each 1/40th of a sec)

    if xloc + 50 > DISPLAY[0]:  #if out of screen
        xloc = DISPLAY[0] - 50  #make it within screen


    ############################
    # 3.Display/Refresh OUTPUT #
    ############################

    #a. clear: fill the background to empty it
    screen.fill((30, 100, 160))

    #b. draw:
    # Rectangle at a location (xloc,yloc) with width 50 ht 20
    pygame.draw.rect(screen,(255,0,255), pygame.Rect(xloc, yloc, 50, 20))
    
    #c. display: flip the page, to display it
    pygame.display.flip()

    #d. Control Framerate. (Optional, include this for better to control) 
    #delay 1/40th of a second every loop, to slow down, to see the animation
    clock.tick(40)

#Out of game loop. Close display
pygame.display.quit()
  
