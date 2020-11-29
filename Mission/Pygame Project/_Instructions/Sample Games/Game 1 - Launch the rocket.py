#Lesson 4: Game loop and Key Inputs
#
#Now that you used a for-loop to do animation, we will now use a while loop
#
#GAME LOOP
#A game loop consists of some elements:
#while True:
#   1. Check INPUT
#   2. PROCESS objects in game
#   3. Display/Refresh OUTPUT
#   4. Control framerate (if required)
#
#
#KEY INPUTS
#There are 2 types of inputs you can process:
#  1. One time events
#  for event in pygame.event.get():
#
#  2. Keys that are held down
#  pressed = pygame.key.get_pressed()
#
#  See how it is implemented in the code below
#  For a list of all possible keypresses,
#  try typing help(pygame) in the python command line/shell,
#  and scrutinise the K_ constants for the one you want.
#
################################################################
#
# Instructions: left/right to move, up to jump
# spacebar is for jet pack

import pygame
import math

#1. Initialise pygame and display

DISPLAY=(400,300) #define size of graphics display
pygame.init()
screen = pygame.display.set_mode(DISPLAY)
clock = pygame.time.Clock() #initialise clock to control framerate

#2. Set up your game variables
done = False
fire=False
yvel=0
xvel=0
xpos=190
ypos=20
is_blue=True
GRAVITY = 0.1
jetpackfuel=100

#3. Game Loop
while done == False:
    #1. INPUT #############################################################
    #1a. Process one time events          <<<<<<<
    #type help(pygame) in command line to see all possible keys to detect    
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_blue = not is_blue
            if event.key == pygame.K_UP and ypos==DISPLAY[1]-30:
                yvel=-3 #if player pressed up, and player is on the ground, jump

    #1b. Process keys that are held down  <<<<<<<<
    pressed = pygame.key.get_pressed() 
    if pressed[pygame.K_SPACE] and jetpackfuel>0:
        fire=True #if user pressed space, and there is fuel, show fire
        yvel-=0.15
        jetpackfuel-=1
    else:
        fire=False
    if pressed[pygame.K_LEFT]:
        xpos-=2
    if pressed[pygame.K_RIGHT]:
        xpos+=2

    #2.PROCESS what happens when 1 unit of time (1/60) sec elapses #########
    ypos+=yvel #Change displacement due to velocity
    xpos+=xvel #Change displacement due to velocity
    yvel+=GRAVITY #Change velocity due to acceleration (gravity)

    if ypos+30>DISPLAY[1]: #if bottom of object goes out of display
        ypos=DISPLAY[1]-30 #make it stop and motionless
        yvel=0

    if jetpackfuel<100:   #Let the jetpackfuel regenerate slowly over time
        jetpackfuel+=0.2  #increase by 0.2 in 1/60th of a second

    #3.Display/Refresh OUTPUT ###############################################
    #Blank out the background layer first.
    screen.fill((0, 0, 0))

    if is_blue: #set the correct color of the rectangle
        color = (0, 128, 255)  
    else:
        color = (255, 128, 0)
    
    #Blit the objects on screen
    pygame.draw.rect(screen, color, pygame.Rect(xpos, ypos, 20, 30))
    
    if fire: #if there is fire, draw one (using the polygon function)
        pygame.draw.polygon(screen,(255,0,0),[(xpos+5,ypos+25), (xpos+15,ypos+25),(xpos+10,ypos+45)],3)

    #Finally, when blitting is done/complete, show it.
    pygame.display.flip()

    #4. Control Framerate. (Optional, better to control) ###################
    #   Assuming code runs in 0 time, this will approximate to 60 fps.
    clock.tick(60)  #Wait 1/60th of a second

#Out of game loop. Close display
pygame.display.quit()
