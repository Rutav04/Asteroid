# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import time
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

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
    Score.containers = (updateable, drawble)
    AsteroidField.containers = updateable

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/ 2)
    score = Score()
    game_running = True
    accumulated_time = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 game_running = False
        
        updateable.update(dt)
        


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
                    score.asteroid_destroyed()
        
        screen.fill((0, 0, 0))
        
        for obj in drawble:
            obj.draw(screen)

        score_text = score.display_score()
        screen.blit(score_text, (10, 10))
      
        pygame.display.flip()
        
        dt = clock.tick(60)/1000
        
        accumulated_time += dt 

        if accumulated_time >= 10:
            score.time_up()  # Increase the score based on elapsed time
            accumulated_time = 0 
        


if __name__ == "__main__":
    main()