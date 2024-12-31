# https://www.youtube.com/watch?v=2gABYM5M0ww&t=235s
# 47:00
import sys

import pygame
# calling PhysicsEntity class in entities file
from scripts.entities import PhysicsEntity
# calling load_image function in utils file
from scripts.utils import load_image

class Game:
    def __init__(self):
        pygame.init()
        # screen caption
        pygame.display.set_caption('Ninja Game')
        # screen size
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]
        # using load_image function in utils file
        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

    def run(self):
        while True:
            self.display.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()