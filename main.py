import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    score = 0
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = pygame.Color(0, 0, 0)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #limit the framerate to 60FPS
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collisionCheck(asteroid):
                    pygame.sprite.Sprite.kill(shot)
                    asteroid.split()
   
        for asteroid in asteroids:
            if player.collisionCheck(asteroid):
                print("Game Over!")
                sys.exit()

        screen.fill(black)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()
