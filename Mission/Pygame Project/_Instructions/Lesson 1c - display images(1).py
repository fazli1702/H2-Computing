###### LESSON 1c ######
#In this lesson, we will transform and display an image.


import pygame
import math

#define size of graphics display
DISPLAY=(400,300)

#compulsory code to initialise pygame and display
pygame.init()
screen = pygame.display.set_mode(DISPLAY)

#fill background with blue colour first 
screen.fill((30, 100, 160))

#Initialising images (If you have a picture file you want to display)
imagebird = pygame.image.load('bird.png')
imagebird2 = pygame.transform.flip(imagebird,True,False)
imagebird3 = pygame.transform.rotate(imagebird,30)
#scale twice the dimensions
imagebird4 = pygame.transform.scale2x(imagebird)
#scale an object to any preferred size
imagebird5 = pygame.transform.smoothscale(imagebird,(20,34))

#Drawing images
#screen.blit(imageobject, xy-coordinates)
screen.blit(imagebird, (80,220))
screen.blit(imagebird2,(120,220))
screen.blit(imagebird3,(160,220))
screen.blit(imagebird4,(200,220))
screen.blit(imagebird5,(280,220))

#Display objects blitted into memory
pygame.display.flip()


