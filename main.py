import pygame, sys
from home import Home
from game import Game

pygame.init()
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height,))
pygame.display.set_caption("Rose Empire")

clock = pygame.time.Clock()

home = Home(screen, screen_width, screen_height)
game = Game(screen, screen_width, screen_height)


home_active = True
game_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            home_active = False
            game_active = True

    if home_active == True:
        home.run()

    if game_active == True:
        game.run()

    pygame.display.flip()
    clock.tick(60)