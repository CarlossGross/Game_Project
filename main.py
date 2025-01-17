import pygame
from constants import *
from circleshape import *
from player import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps_maximizer = pygame.time.Clock()
dt = 0

#create the player instance
playr = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

def main ():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# infinite loop
    i=0
    while i == 0:

# make quit button on window work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
# make screen black    
        screen.fill((0,0,0))

# draw the player
        playr.draw(screen)


# make screen update on every iteration of infinite loop - must be the final of the loop
        pygame.display.flip()

# maximize fps on 60FPS
        dt = fps_maximizer.tick(60)/1000




if __name__ == "__main__":
    main ()