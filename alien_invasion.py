import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    '''Overall class to manage game assets and behaviour'''

    def __init__(self):
        '''Initialise the game, and create game resources'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height, ))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

        # Set background colour.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

                    # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visable.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance.
    ai = AlienInvasion()
    ai.run_game()
