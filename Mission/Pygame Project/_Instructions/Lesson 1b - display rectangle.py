###### LESSON 1b ######
#In this lesson, we will draw some standard shapes.

import pygame
import math

#define size of graphics display
DISPLAY=(400,300)

#compulsory code to initialise pygame and display
pygame.init()
screen = pygame.display.set_mode(DISPLAY)

#fill background with blue colour first 
screen.fill((30, 100, 160))

#Drawing standard shapes
#pygame.draw.rect(Surface, color, rectangle(xcoord,ycoord,xlength,yheight), line width(optional))
pygame.draw.rect(screen,(0,0,255), pygame.Rect(80, 5, 50, 20))
pygame.draw.rect(screen,(255,0,0), pygame.Rect(80, 30, 50, 20),1)

#Display objects blitted into memory
pygame.display.flip()


''' Other standard shapes:
#pygame.draw.ellipse(Surface, color, rectangle, ellipse width(optional))
#The ellipse fills the rectangle defined
pygame.draw.ellipse(screen,(0,255,0),pygame.Rect(80, 55, 50, 20))
pygame.draw.ellipse(screen,(0,255,0),pygame.Rect(180, 55, 50, 20),5) #width 5

#drawing an arc is similar to drawing an ellipse. Angle is in radians.
#It draws part of the ellipse, based on the angle.
pygame.draw.arc(screen,(0,255,0),pygame.Rect(280, 55, 50, 20),math.pi/2,math.pi,3)

#Line with no anti-aliasing
#pygame.draw.line(screen,color,coord1,coord2,line thickness(optional))
pygame.draw.line(screen,pygame.Color('brown'),(180,80),(230,100),3)

#Lines with anti-aliasing
pygame.draw.aaline(screen,(0,0,255),(80,80),(130,100),3)
pygame.draw.aalines(screen,(0,0,255),True,[(80,100), (90,110),(80,110)])
pygame.draw.aalines(screen,(0,255,255),False,[(120,100), (130,110),(120,110)])

#Drawing Circle  (screen, colour, position, radius, width)
pygame.draw.circle(screen,(255,0,0),(80,130),10)

#Drawing polygon (screen, colour, [list of coords], width)
pygame.draw.polygon(screen,(255,255,255),[(80,160), (90,180),(50,180)])
'''
