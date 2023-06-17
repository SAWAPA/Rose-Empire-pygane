import pygame
from player import Player
from coin import Coin
from enemy import Enemy
from random import randint


class Game():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.bg_image = pygame.image.load('assests/12.png').convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))

        #player
        player_sprite = Player((self.screen_width / 2, self.screen_height - 100), self.screen_width)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.score = 0

        #coin
        coin_sprite = Coin(self.screen_width, self.screen_height)
        self.coin = pygame.sprite.Group(coin_sprite)
        self.coin_adding_time = randint(30, 50)

        #enemy
        enemy_sprite = Enemy(self.screen_width, self.screen_height)
        self.enemy = pygame.sprite.Group(enemy_sprite)
        self.enemy_adding_time = randint(40, 50)

        self.gameover = False

    def add_coin(self):
        self.coin_adding_time -= 1
        if self.coin_adding_time <= 0:
            self.coin.add(Coin(self.screen_width, self.screen_height))
            self.coin_adding_time = randint(30, 50)

    def add_enemy(self):
        self.enemy_adding_time -= 1
        if self.enemy_adding_time <= 0:
            self.enemy.add(Enemy(self.screen_width, self.screen_height))
            self.enemy_adding_time = randint(40, 50)


    def collision(self):
        for coin in self.coin:
            if pygame.sprite.spritecollide(coin, self.player, False):
                coin.kill()
                self.score += 1

        for enemy in self.enemy:
            if pygame.sprite.spritecollide(enemy, self.player, False):
                self.gameover = True


    def run(self):
        self.screen.blit(self.bg_image, (0, 0))

        if not self.gameover:
            self.player.draw(self.screen)
            self.player.update()

            self.coin.draw(self.screen)
            self.coin.update()
            self.add_coin()

            self.enemy.draw(self.screen)
            self.enemy.update()
            self.add_enemy()

            self.collision()
