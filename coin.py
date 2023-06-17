import pygame
from random import randint

class Coin(pygame.sprite.Sprite):
    def __init__(self, max_x, max_y):
        super().__init__()
        self.max_x = max_x
        self.max_y = max_y

        coin0 = pygame.image.load('assests/coin/coin0.png')
        coin1 = pygame.image.load('assests/coin/coin1.png')
        coin2 = pygame.image.load('assests/coin/coin2.png')
        coin3 = pygame.image.load('assests/coin/coin3.png')

        coin0 = pygame.transform.scale(coin0, (30, 30))
        coin1 = pygame.transform.scale(coin1, (30, 30))
        coin2 = pygame.transform.scale(coin2, (30, 30))
        coin3 = pygame.transform.scale(coin3, (30, 30))

        self.coin = [coin0, coin1, coin2, coin3]
        self.frame_index = 0

        self.image = self.coin[self.frame_index]
        self.rect = self.image.get_rect(center=(randint(20, self.max_x - 20), -10))

        self.coin_speed = 4

    def running(self):
        self.rect.y += self.coin_speed

    def coin_kill(self):
        if self.rect.y >= self.max_y:
            self.kill()

    def animation(self):
        self.frame_index += 0.2
        if self.frame_index >= len(self.coin):
            self.frame_index = 0

        self.image = self.coin[int(self.frame_index)]

    def update(self):
        self.running()
        self.coin_kill()
        self.animation()
