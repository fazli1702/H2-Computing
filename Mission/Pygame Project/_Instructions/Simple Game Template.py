# This is a simple template to help you get started.
#
# Instructions:
# 1. Press left/right/up/down to move the rectangle
# 2. Press ESC key to close the game screen


import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        #input
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                        is_blue = not is_blue
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                         break

        if done == True:
                pygame.display.quit()
                break
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_SPACE]: is_blue = not is_blue
        if pressed[pygame.K_ESCAPE]: break

        #process
        pass

        #output
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()

        #wait
        clock.tick(60)

#Out of game loop. Close display
pygame.display.quit()
