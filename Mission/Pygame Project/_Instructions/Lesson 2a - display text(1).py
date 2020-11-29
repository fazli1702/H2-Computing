#How to get the R/G/B values of a color?
#
#>>> pygame.Color('red')
#(255, 0, 0, 255)
#>>> pygame.Color('green')
#(0, 255, 0, 255)
#>>> pygame.Color('pink')
#(255, 192, 203, 255)
#
#The first 3 numbers describes amount of Red, Green Blue.
#The last number, Alpha, is for transparancy which is not required for now.



###### LESSON 2a ######
#In this lesson, we will place some text on the pygame screen.


import pygame
import math

#define size of graphics display
DISPLAY=(400,300)

#compulsory code to initialise pygame and display
pygame.init()
screen = pygame.display.set_mode(DISPLAY)

#fill background with blue colour first 
screen.fill((30, 100, 160))

#if default font exists, use it
if pygame.font:
    font = pygame.font.Font(None,40)  #40 is the font height
else:
    font = None

#Syntax: screen.blit(font.render("your text to display", Antialiasing? T/F, colour), xy-coord)
# With 'Antialiasing' set to True, the text display should be smoother.

screen.blit(font.render("Example 1", False, (0,0,0)), (5,10))  #(0,0,0) is black
screen.blit(font.render("Example 2", True, (255,0,0)), (5,200)) #(255,0,0) is red


#Display objects blitted into memory
pygame.display.flip()


