import pygame

class Ship():
    def __init__(self, game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for ship's center
        self.center = float(self.rect.centerx)

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flag"""
        # update ship's center value not rect
        if self.moving_right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.game_settings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
