# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawble = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawble)
    Shot.containers = (shots, updateable, drawble)
    Asteroid.containers =(asteroids, updateable, drawble)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/ 2)
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        for obj in updateable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
        
        screen.fill((0, 0, 0))
        
        for obj in drawble:
            obj.draw(screen)

      
        pygame.display.flip()
        
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()