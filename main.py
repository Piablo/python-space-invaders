import pygame, sys
from player import Player
from alien import Alien

class Game:
    def __init__(self):
        #Player setup
        player_sprite = Player((screen_width / 2, screen_height), screen_width,  5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)
    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)                                          #Lesson2
        self.player.draw(screen)
        self.aliens.draw(screen)
    def alien_setup(self, rows, cols, x_distance = 60, y_distance=48, x_offset = 70, y_offset = 100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0: alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2: alien_sprite = Alien('green', x, y)
                else: alien_sprite = Alien('red', x, y)

                self.aliens.add(alien_sprite)

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((45,45,55))
        game.run()
        pygame.display.flip()
        clock.tick(60)