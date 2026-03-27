import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, game_settings, screen, ship):
        """Create bullet object at ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet object at (0, 0) and set correct position
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullet's position as decimal value
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """move the bullet up the screen"""
        # update decimal position
        self.y -= self.speed_factor
        # update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
