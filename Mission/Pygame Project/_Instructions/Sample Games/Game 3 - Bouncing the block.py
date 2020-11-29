# Lesson 5 Using Functions, Using GAMESTATE, Documenting your code
# In this lesson, there are 3 points to highlight
#
# 1. Functions/Procedures: #######
# We can write functions/procedures to tidy up the code, to make it look neater.
# The code is nearly the same, it is just placed in functions called
# get_input, process_game_objects, and display.
# nonlocal is used to differentiate/access/edit whether the
# variables belong in main() or belong in the function.
#
# The disadvantage of using functions is that it can be more difficult to
# debug when something goes wrong, since you can't check variables as easily.
#
# 2. Gamestates: #######
# We can introduce GAMESTATES to control the flow of the game
# Here, 0 represents running, 1 represents paused, 2 represents quit
# Refer to the code below how Gamestates can be implemented
#
# If gamestate == 1, we do not perform some lines of code.
# but we will still need to check for input 'p' to unpause.
# 
# 3. Documentation:  #######
# Try to document what your code/game does.
# For example, see the Instructions below, and do the same for your code:
# to inform the user what your code can do.
#
# Constraints:
# (Note that the square object is now constraint to be bounded within the
# left/right boundaries of the display screen)
#
#######################################################################
#
# Instructions:
# The code below attempts to simulate a box bouncing, with a bounce counter.
#
# Use left/right/up/down arrow keys to move the box, and space to change colour
# p to pause, Escape to quit

import pygame

def main():
    
    #this is the function to check input for the game loop
    def get_input():
        nonlocal is_blue, x, y, GAMESTATE, yvel #declare game variables you are going to access

        #process one time events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAMESTATE = 2 #if click on [X], quit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                GAMESTATE = 2 #if press Esc, quit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue #flip colour
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                is_blue = not is_blue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                if GAMESTATE == 1: #flip between pause and play
                    GAMESTATE=0
                else:
                    GAMESTATE = 1
        if GAMESTATE == 1:
            return
        #process keys that are held down here
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y-=3
        if pressed[pygame.K_DOWN]:
            if y!=240 and yvel!=0:
                y += 3
        if pressed[pygame.K_LEFT] and x >0: x -= 3
        if pressed[pygame.K_RIGHT] and x < 340: x += 3
        #if pressed[pygame.K_SPACE]: is_blue = not is_blue  #<<<<<<<<
        #Does not change colour correctly. Should process this as a one-time event

    #this is the function to process gravity, velocity, and displacement in game loop
    #i.e. the game engine
    def process_game_objects():
        nonlocal x,y,yvel,is_blue,bounces  #declare game variables you are going to access

        y+=yvel  # update distance with to velocity value
        sunk=(y+60)-300  #calculate how deep sunk into floor
        if sunk>=0:      #if it is on floor, or hits through floor...
            if 0<=sunk<0.6 and yvel<0.6: #if it is near motionless,
                y=240  #make it lie exactly on the floor
                yvel=0 #make it motionless. Don't apply gravity
            else: #else, process it bouncing
                bounces+=1 
                is_blue = not is_blue 
                y=240-sunk     #reflect it up (to conserve dist moved)
                yvel=-yvel*0.9 #since it bounced, change the yvel to go up, with some velocity loss
                yvel+=0.15     #Apply gravity
        else:
            yvel+=0.15 #Apply gravity
        #print(sunk,yvel) for debugging

    #this is the function to display on screen
    def display():
        screen.fill((0, 0, 0))  #blank out the screen (lowest layer)

        #draw the text (middle layer)
        font_surface = font.render("Bounces: " + str(bounces), False, (255,255,255))
        screen.blit(font_surface, (5,5))   
        #draw the square (upper layer)
        if is_blue: color = (0, 128, 255)  #set the correct color
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) #then draw it        

        #display the paused text if paused (1)
        if GAMESTATE==1:
            screen.blit(font.render("Paused",False,(255,255,255)),(150,140))

        pygame.display.flip() #update the display to show to the user

    #initialise pygame and game variables
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((400, 300))
    font = pygame.font.Font(None,30)
    GAMESTATE = 0
    is_blue = True
    x = 175
    y = 50
    yvel=0
    bounces=0

    #game loop
    while GAMESTATE != 2:
        get_input()            #input
        if GAMESTATE==0:       #if game is running (0), and not paused
            process_game_objects() #do the game processing
        display()              #output
        clock.tick(60)         #wait

    #close display when out of game loop
    pygame.display.quit()


if __name__ == "__main__":  #runs the function main() automatically
    main()
