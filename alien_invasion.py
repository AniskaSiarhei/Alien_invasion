import pygame
from pygame.sprite import Group
from game_stats import GameStats
import game_functions as game_f
from alien import Alien
from settings import Settings
from ship import Ship
from button import Button
from scoreboard import Scoreboard


def run_game():
    # initial game
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    game_f.create_fleet(ai_settings, screen, ship, aliens)

    # run game
    while True:
        game_f.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            game_f.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            game_f.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        game_f.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()