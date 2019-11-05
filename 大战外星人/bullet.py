import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_setting, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_witch, ai_setting.bullet_hight)
        self.rect.centerx = ship.rect.centerx



