import pygame
from random import randint
import numpy as np


class Game(object):

    def __init__(self, width=20, heigth=20, game_speed=30, display_option=True):
        self.game_width = width * 20 + 40
        self.game_height = heigth * 20 + 40
        self.width = width
        self.height = heigth

        if display_option is True:
            self.gameDisplay = pygame.display.set_mode(
                (self.game_width, self.game_height + 100))
            # self.bg = print
            pygame.display.set_caption('Snake')
        self.player = []
        self.food = []
        self.display_option = game_speed
 # Retorna ñas coordenadas de las ubicaciones libres

    def find_free_space(self):
        x_rand = randint(20, self.game_width - 40)
        x = x_rand - x_rand % 20
        y_rand = randint(20, self.game_height - 40)
        y = y_rand - y_rand % 20
        for player in self.players:
            if [x, y] not in player.position:
                return x, y
            else:
                return self.find_free_space()


s = Game()
print(s.find_free_space())
