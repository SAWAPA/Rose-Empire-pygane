import pygame

class Home():
    def __init__(self, screen, screen_width, screen_height):

        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.bg_image = pygame.image.load('assests/12.png').convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (1600, 1000))

        #font
        self.font = pygame.font.Font('assests/fibberish.ttf', 100)

    def run(self):
        self.screen.blit(self.bg_image, (0, 0))

        title_surf = self.font.render('Rose Empire', False, 'green')
        title_rect = title_surf.get_rect(center = (self.screen_width / 2, self.screen_height / 2))
        self.screen.blit(title_surf, title_rect)