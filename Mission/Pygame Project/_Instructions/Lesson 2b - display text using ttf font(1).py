###### LESSON 2b ######
#In this lesson, we will load and use a True Type Font (ttf).
#Note: The ttf font file must be kept in the same folder as the python code.


import pygame

import sys, os
try:
    import pygame.freetype as freetype
except ImportError:
    print ("No FreeType support compiled")
    sys.exit ()

#define size of graphics display
DISPLAY=(400,300)

#compulsory code to initialise pygame and display
pygame.init()
screen = pygame.display.set_mode(DISPLAY)

#find the font in the directory structure
fontdir = os.path.dirname(os.path.abspath (__file__))
font = freetype.Font(os.path.join (fontdir, "", "sans.ttf"))

#fill background with blue colour first 
screen.fill((30, 100, 160))

#render the font using method 1:
# (255,255,0) is yellow, (0,255,0) is green
#Syntax : font.render_to(screen, xy-coord, "your text", foreground colour, background colour, style, rotation)
font.render_to(screen, (5, 10), "Method 1", (255,255,0), (0,255,0), size=30, style=freetype.STYLE_UNDERLINE|freetype.STYLE_OBLIQUE)

#render the font using method 2:
#Syntax : font.render("your text", foreground colour, background colour, style, rotation,size)
font_surface = font.render("Method 2",(255,255,0),(0,255,0),size=40)
#screen.blit(yourfont, xy-coord)
screen.blit(font_surface[0], (5,200))

#Display objects blitted into memory
pygame.display.flip()


