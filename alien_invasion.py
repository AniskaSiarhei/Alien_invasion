import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as game_f
from pygame.sprite import Group

def run_game():
    # initial game
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    bullets = Group()

    # run game
    while True:
        game_f.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        game_f.update_bullets(bullets)

        game_f.update_screen(ai_settings, screen, ship, bullets)

run_game()