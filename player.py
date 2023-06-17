import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, max_x):
        super().__init__()
        self.max_x = max_x

        run0 = pygame.image.load('assests/player/run0.png')
        run1 = pygame.image.load('assests/player/run1.png')
        run2 = pygame.image.load('assests/player/run2.png')
        run3 = pygame.image.load('assests/player/run3.png')
        run4 = pygame.image.load('assests/player/run4.png')
        run5 = pygame.image.load('assests/player/run5.png')
        run6 = pygame.image.load('assests/player/run6.png')
        run7 = pygame.image.load('assests/player/run7.png')

        run0 = pygame.transform.scale(run0, (150, 150))
        run1 = pygame.transform.scale(run1, (150, 150))
        run2 = pygame.transform.scale(run2, (150, 150))
        run3 = pygame.transform.scale(run3, (150, 150))
        run4 = pygame.transform.scale(run4, (150, 150))
        run5 = pygame.transform.scale(run5, (150, 150))
        run6 = pygame.transform.scale(run6, (150, 150))
        run7 = pygame.transform.scale(run7, (150, 150))

        self.run = [run0, run1, run2, run3, run4, run5, run6, run7]
        self.frame_index = 0

        self.image = self.run[self.frame_index]
        self.rect = self.image.get_rect(midbottom = pos)

        self.speed = 5

        self.facing_right = True

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed = -5
            self.facing_right = False
        if keys[pygame.K_RIGHT]:
            self.speed = 5
            self.facing_right = True

    def running(self):
        self.rect.x += self.speed

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.x = 0
        if self.rect.right >= self.max_x:
            self.rect.right = self.max_x

    def animation(self):
        self.frame_index += 0.2
        if self.frame_index >= len(self.run):
            self.frame_index = 0

        self.image = self.run[int(self.frame_index)]

        if not self.facing_right:
            self.image = pygame.transform.flip(self.run[int(self.frame_index)], True, False)

    def update(self):
        self.get_input()
        self.running()
        self.constraint()
        self.animation()
