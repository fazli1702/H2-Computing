# 1. Using Functions to organise the codes
#    The whole game code is wrapped within the main() function;
#    it contains the get_input(), process_game_objects() and display() functions.
#    - the game variables are initialised in the main() function
#    - these game variables need to be declared as nonlocal within the
#      get_input(), process_game_objects() and display() functions.
#
# 2. Gamestates (0/1/2)
#    We can introduce GAMESTATES to control the flow of the game.
#    0 : run the game
#    1 : pause the game
#    2 : quit the game
#
# 3. Documentation
#    It is important to use version and comment to document the game development.
#    This will help the reader to understand the purpose of certain lines of codes.



###### LESSON 5 ######
#In this lesson, we will use functions to organise the codes
#and GAMESTATE to control the game.
#
# Instructions:
# 1. Press left/right/up/down to move the rectangle
# 2. Press ESC key to close the game screen
# 3. Click within the rectangle to play a sound
# 4. Press 'p' to toggle between PAUSE/PLAY


import pygame
import math

def main():
    #initialise pygame
    pygame.init()
    clock = pygame.time.Clock()

    #display
    DISPLAY=(400,300)
    screen = pygame.display.set_mode(DISPLAY)
    screen.fill((30, 100, 160))
    font = pygame.font.Font(None,30)

    #sound
    pygame.mixer.pre_init(44100, -16, 2, 512) #initialise pygame sound
    boomsound=pygame.mixer.Sound("boom.wav")  #load boom.wav sound file
    boomsound.set_volume(60)                  #set its volume

    #game variables
    xloc = 10
    yloc = 100
    GRAVITY = 1
    GAMESTATE = 0

    def get_input():
        nonlocal xloc, yloc, GAMESTATE, GRAVITY #declare game variables you are going to access

        ############
        # 1. INPUT #
        ############

        #>>>>>  1a. Process one time events  <<<<<
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                GAMESTATE = 2
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
                    GAMESTATE = 2
                    
                #toggle between pause and play
                if event.key == pygame.K_p:
                    if GAMESTATE == 0:
                        GAMESTATE = 1
                        print("User paused the game")
                    elif GAMESTATE == 1:
                        GAMESTATE = 0
                        print("User unpaused the game")

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
            GAMESTATE = 2


    #############
    # 2.PROCESS #
    #############
    def process_game_objects():
        nonlocal xloc, yloc, GAMESTATE, GRAVITY #declare game variables you are going to access

        xloc+=1  #moves the rectangle 1 pixel right each frame (each 1/40th of a sec)
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
    def display():
        #a. clear: fill the background to empty it
        screen.fill((30, 100, 160))

        #b. draw:
        # Rectangle at a location (xloc,yloc) with width 50 ht 20
        pygame.draw.rect(screen,(255,0,255), pygame.Rect(xloc, yloc, 50, 20))
        
        #display the paused text if paused (1)
        if GAMESTATE==1:
            screen.blit(font.render("Paused",False,(255,255,255)),(150,140))

        #c. display: flip the page, to display it
        pygame.display.flip()

        #d. Control Framerate. (Optional, include this for better to control) 
        #delay 1/40th of a second every loop, to slow down, to see the animation
        clock.tick(40)


    #Game Loop
    while GAMESTATE != 2:
        get_input()
        if GAMESTATE == 0:         #if game is running (0), and not paused
            process_game_objects() #do the game processing
        display()                  #output


    #Out of game loop. Close display
    pygame.display.quit()

if __name__ == "__main__":  #runs the function main() automatically
    main()  
