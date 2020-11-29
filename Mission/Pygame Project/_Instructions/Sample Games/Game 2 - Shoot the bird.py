# Lesson 7 Mouse Input and Sounds
#
# The pygame code to check for mouse click,
# can be found at the check_input() function
#
# The code to initialise and load and play sounds can be found below
#
###########################################################################
#
# Instructions:
# bird: up/down/left/right arrow keys to move bird
# Clicking the bird with the mouse will cause it to complain with a sound
# Escape or [X] ends program

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" #Removes pygame starting text
import pygame #if you import both at the same time, you will still see start text.

def main():
    #initialise pygame sound (if you are using sound)
    pygame.mixer.pre_init(44100, -16, 2, 512)

    #initialise pygame game clock (if you are controlling frame rate)
    clock = pygame.time.Clock()
    time = 0 

    #compulsory code to initialise pygame
    pygame.init()

    #set up size of screen
    DISPLAY=(800,300)
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("XYZ's Game") #Personalise app text

    #setup font, in preparation to display text in graphics screen
    if pygame.font:
        font = pygame.font.Font(None,20)  #20 is the font height
    else:
        font = None

    #Initialise bird in game
    birdx, birdy = 50, 50
    birdfaceright=True
    imagebird = pygame.image.load('bird.png') #this is a 34 wide x 24 tall picture
    imagebird2 = pygame.transform.flip(imagebird,True,False) #this is the bird facing left
    birdsound=pygame.mixer.Sound("birdsound.wav") #initialise sound
    birdsound.set_volume(80)
    boomsound=pygame.mixer.Sound("boom.wav") #initialise sound
    boomsound.set_volume(80)
    boomsoundplaying=0
    birdsoundplaying=0 #to monitor if bird sound is playing. 

    drawtext=[]
    #drawtext=[(100,150,"My Game",(255,0,0)),(200,200,"Eg",(0,255,0))]  #example where you want to place some text at some coord with choice of colour

    #Initialise game variables
    GAMESTATE=0 #0 means running, 1 means pause, 2 means end

    #Makes windows mouse cursor invisible because we will be
    pygame.mouse.set_visible(False) #replacing mouse cursor with target scope

    def check_input():
        #declare the variables that you could possibly be modifying
        nonlocal birdx, birdy, GAMESTATE, birdsoundplaying,boomsoundplaying

        #detecting mouse clicks, or short key presses
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.dict["key"]==pygame.K_ESCAPE:
                GAMESTATE=2
            if event.type == pygame.QUIT:
                GAMESTATE=2
            if event.type == pygame.MOUSEBUTTONDOWN: #if there is a mouseclick
                #event.dict["pos"] stores the (x,y) coordinate where it is clicked
                if boomsoundplaying==0: #if the gun has cooled down, fire gun
                    boomsound.play()
                    boomsoundplaying=60 #disallow the gun from being fired for 60 frames
                    if birdx<event.dict["pos"][0]<birdx+34 and birdy<event.dict["pos"][1]<birdy+24:
                        if birdsoundplaying==0: #if the mouseclick is on the bird
                            birdsound.play()    #and the bird is not already complaining
                            birdsoundplaying=60 #play sound. Disallow bird from complaining for 60 frames
        #detecting buttons that are held down for long duration
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:   #moves bird 2 pixels up (up is negative)
            birdy -= 2
        if pressed[pygame.K_DOWN]: #moves bird 2 pixels down
            birdy += 2
        if pressed[pygame.K_LEFT]: #moves bird 2 pixels left
            birdx -= 2
            birdfaceright=False
        if pressed[pygame.K_RIGHT]:#moves bird 2 pixels right
            birdx += 2
            birdfaceright=True

    def process(): #process the data in game to update frame by frame
        nonlocal birdx, birdy, GAMESTATE, birdsoundplaying, time, boomsoundplaying
        if birdx<0:  #if bird goes too far to the left of display window
            birdx=0  #restrict its location to just within window

        if birdx+34>DISPLAY[0]: #if bird goes right of display window
            birdx=DISPLAY[0]-34

        if birdy<0: #if bird goes above display window
            birdy=0

        if birdy+24>DISPLAY[1]: #if bird goes below display window
            birdy=DISPLAY[1]-24

        if birdsoundplaying>0:    #update bird sound as time elapses
            birdsoundplaying-=1
        if boomsoundplaying>0:    #update boom sound as time elapses
            boomsoundplaying-=1
        time+=1   #1 frame/unit of time elapsed (1/60th of a second)

        #make the bird fall by default
        birdy+=1  #1 pixel per frame

    def draw_screen():
        #Remember to draw your objects in order of lower layer to upper layer

        #Background layer
        #reset background to all black (0,0,0)
        screen.fill((0, 0, 0))

        #Text layer        
        #displays any text you have in the list drawtext
        for x,y,txt,colour in drawtext: 
            screen.blit(font.render(txt, False, colour), (x,y))

        #display time at top left corner
        screen.blit(font.render("Time: "+str(int(time/60)), False, (255,255,255)), (0,0))

        #Objects of Interest in Game
        #display bird with correct orientation
        if birdfaceright:       
            screen.blit(imagebird, (birdx,int(birdy)))
        else:
            screen.blit(imagebird2, (birdx,int(birdy)))

        #draw the targetting scope using 1 circle, 1 ellipse, and 2 lines
        coord = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255,0,0), coord, 30,2)
        pygame.draw.line(screen,(255,0,0), (coord[0],coord[1]-30),(coord[0],coord[1]+30),2)
        pygame.draw.line(screen,(255,0,0), (coord[0]-30,coord[1]),(coord[0]+30,coord[1]),2)
        pygame.draw.ellipse(screen,(255,0,0),pygame.Rect(coord[0]-45,coord[1]-30,90,60),4)

        #Update the display
        pygame.display.flip()   
        
    # Main Loop

    while GAMESTATE==0 or GAMESTATE == 1:
        check_input()
        process()
        draw_screen()
        clock.tick(60) #wait 1/60th of a second
    

if __name__ == '__main__':
    main()

pygame.display.quit()
