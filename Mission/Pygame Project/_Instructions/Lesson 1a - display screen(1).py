###### LESSON 1a ######
#In this lesson, we will define and display a pygame screen.


import pygame
import math

#define size of graphics display
DISPLAY=(400,300)

#compulsory code to initialise pygame and display
pygame.init()
screen = pygame.display.set_mode(DISPLAY)

#fill background with blue colour first 
screen.fill((30, 100, 160))

#Display objects blitted into memory
pygame.display.flip()
