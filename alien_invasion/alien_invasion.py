import sys

import pygame

from ship import Ship
from settings import Settings


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraw the screen during each pass through the loop
        screen.fill(game_settings.bg_color)
        ship.blitme()

        # make the most recently drawn screen visible
        pygame.display.flip()

run_game()
