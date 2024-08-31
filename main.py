from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

import sys
import pygame

from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateables, drawables)
    Asteroid.containers = (updateables, drawables, asteroids)
    AsteroidField.containers = (updateables)
    Shot.containers = (updateables, shots, drawables)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color='BLACK')

        for drawable in drawables:
            drawable.draw(screen)

        for updateable in updateables:
            updateable.update(dt)

        for asteroid in asteroids:
            for bullit in shots:
                if asteroid.checkForCollision(bullit):
                    bullit.kill()
                    asteroid.split()
            if asteroid.checkForCollision(player1):
                print("Game over!")
                sys.exit()


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
