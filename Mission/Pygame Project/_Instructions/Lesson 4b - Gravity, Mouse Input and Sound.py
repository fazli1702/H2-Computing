
###### LESSON 4B ######
#In this lesson, we will include the following:
#   - Object falling due to GRAVITY (line 38 and 95)
#   - Detecting mouse click and playing a sound. (Lines 25-28 and 65-69)
#
# Instructions:
# 1. Press left/right/up/down to move the rectangle
# 2. Press ESC key to close the game screen
# 3. Click within the rectangle to play a sound


import pygame
import math

#define size of graphics display
DISPLAY=(400,300)

#initialise the pygame game clock
clock = pygame.time.Clock()

#initialise pygame and display
pygame.init()
screen = pygame.display.set_mode(DISPLAY)

#initialise sound
pygame.mixer.pre_init(44100, -16, 2, 512) #initialise pygame sound
boomsound=pygame.mixer.Sound("boom.wav")  #load boom.wav sound file
boomsound.set_volume(60)                  #set its volume

#fill background with blue colour first 
screen.fill((30, 100, 160))

#initialise game variables
xloc = 10
yloc = 100
done = False
GRAVITY = 1

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

        if event.type == pygame.MOUSEBUTTONDOWN: #if there is a mouseclick
            mousex, mousey = event.dict["pos"]   #get the coordinates
            print("Mouse click at coords",mousex,mousey)
            if xloc < mousex < xloc+50 and yloc < mousey < yloc+20: 
                boomsound.play() #play the sound if click within the rectangle


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

    #xloc+=1  #moves the rectangle 1 pixel right each frame (each 1/40th of a sec)
    yloc+=GRAVITY
    
    #keep the rectangle within the screen
    if xloc < 0:
        xloc = 0

    if yloc < 0:
        yloc = 0

    if xloc + 50 > DISPLAY[0]:  
        xloc = DISPLAY[0] - 50  

    if yloc + 20 > DISPLAY[1]:  
        yloc = DISPLAY[1] - 20  


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
  
