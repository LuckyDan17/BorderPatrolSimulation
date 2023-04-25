from BorderPatrolSimulation.Entities.CircleEntities.CircleEntity import CircleEntity
from BorderPatrolSimulation.Entities.Entity import Entity
from BorderPatrolSimulation.Settings.Constants import *
import pygame


class Base(CircleEntity):

    BaseRadius = Constants["Entity"]["Base"]["Radius"]
    
    def __init__(self, radius=None, image_path=None, color=None):
        if "Base" in Entity.EntityGroupRegister:
            raise TypeError("Only one Base could exist!")
        super().__init__((0, 0, 0), Base.BaseRadius, 0, image_path, color)
        self._is_alive = True
        if self.image is None:
            self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        else:
            self.image = self.image
        # self.rect = self.image.get_rect(center=self.center_coord)
        self.rect = self.image.get_rect()

    @property
    def is_alive(self):
        return self._is_alive

    def kill(self):
        self._is_alive = False
