import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("controller input example")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
clock = pygame.time.Clock() #set up clock

xpos = 50
ypos = 50

controller = pygame.joystick.Joystick(0) 
controller.init()
    
while True:#game loop--------------------------------------------------------
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #close game window
            pygame.quit()

    xVel = controller.get_axis(0) #returns a number b/t -1 and 1
    yVel = controller.get_axis(1) #returns a number b/t -1 and 1

    xpos += int(xVel * 10)
    ypos += int(yVel * 10)
 
    #render section--------------------
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,0), (xpos, ypos, 20, 20))
    pygame.display.flip()
#end game loop-------------------------------------------------------------------    

pygame.quit()
