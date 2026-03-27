import sys

import pygame

from pygame.sprite import Group

from ship import Ship
from settings import Settings
import game_functions as gf


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(game_settings, screen)
    # make a group to store bullets
    bullets = Group()

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(game_settings, screen, ship, bullets)

run_game()
