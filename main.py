import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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
    
        screen.fill(black)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()