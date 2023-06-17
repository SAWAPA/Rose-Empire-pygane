import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self, max_x, max_y):
        super().__init__()
        self.max_x = max_x
        self.max_y = max_y

        enemy0 = pygame.image.load('assests/enemy/enemy0.png')
        enemy1 = pygame.image.load('assests/enemy/enemy1.png')
        enemy2 = pygame.image.load('assests/enemy/enemy2.png')
        enemy3 = pygame.image.load('assests/enemy/enemy3.png')

        enemy0 = pygame.transform.scale(enemy0, (30, 30))
        enemy1 = pygame.transform.scale(enemy1, (30, 30))
        enemy2 = pygame.transform.scale(enemy2, (30, 30))
        enemy3 = pygame.transform.scale(enemy3, (30, 30))

        self.enemy = [enemy0, enemy1, enemy2, enemy3]
        self.frame_index = 0

        self.image = self.enemy[self.frame_index]
        self.rect = self.image.get_rect(center = (randint(20, self.max_x - 20), -10))

        self.enemy_speed = 4

    def running(self):
        self.rect.y += self.enemy_speed

    def enemy_kill(self):
        if self.rect.y >= self.max_y:
            self.kill()

    def update(self):
        self.running()