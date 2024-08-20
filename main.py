import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable.add(player, asteroids)
    drawable.add(player, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Update all sprites in the updatable group
        for sprite in updatable:
            sprite.update(dt)

        # Draw all sprites in the drawable group
        for sprite in drawable:
            sprite.draw(screen)

        for obj in asteroids:
            if obj.check_collisions(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
