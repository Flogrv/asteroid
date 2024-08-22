import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mixer.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable.add(player, asteroids)
    drawable.add(player, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    while True:
        font = pygame.font.Font(None, 36)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for obj in asteroids:
            if obj.check_collisions(player):
                print("Game over!")
                print(score)
                sys.exit()
            for shot in shots:
                if shot.check_collisions(obj):
                    obj.split()
                    shot.kill()
                    score += SCORE_INCREMENT
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
