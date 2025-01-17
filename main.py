import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps_maximizer = pygame.time.Clock()
dt = 0

# creating containers and assigning elements on containers
updatabe = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
AsteroidField.containers = (updatabe)
Player.containers = (updatabe, drawable)
Asteroid.containers = (asteroids, updatabe, drawable)

#create the player instance
playr = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# create de asteroids field instance
field = AsteroidField()

def main ():
    global dt
    
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

# draw the drawable container items
        for item in drawable:
             item.draw(screen)

# update the updatable container items
        for item in updatabe:
             item.update(dt)

# teste if any asteroid collide with player and end the game if so
        for item in asteroids:
            if item.collide_test(playr):
                print("Game over!")
                return

# make screen update on every iteration of infinite loop - must be the final of the loop
        pygame.display.flip()

# maximize fps on 60FPS
        dt = fps_maximizer.tick(60)/1000
        #print(dt)




if __name__ == "__main__":
    main ()