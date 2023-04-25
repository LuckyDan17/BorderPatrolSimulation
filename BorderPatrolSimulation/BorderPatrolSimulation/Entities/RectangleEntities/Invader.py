from BorderPatrolSimulation.Entities.RectangleEntities.RectangleEntity import RectangleEntity
from BorderPatrolSimulation.Settings.Constants import Constants
import pygame


class Invader(RectangleEntity):

    Register = pygame.sprite.Group()
    InvaderSize = Constants["Entity"]["Invader"]["Size"]
    SpawnRadius = Constants["Entity"]["Invader"]["SpawnRadius"]
    CollideRectRatio = Constants["Entity"]["Invader"]["CollideRectRatio"]

    def __init__(self, size=None, speed=None, image_path=None, color=None):
        super().__init__((0, 0, 0), size if size is not None else Invader.InvaderSize, speed, image_path, color)
        self.image = pygame.Surface((self.width, self.length), pygame.SRCALPHA)
        self.image.fill(color)
        self.set_spawn_coords(radius=Invader.SpawnRadius)
        while pygame.sprite.spritecollide(self, Invader.Register, False,
                                          pygame.sprite.collide_rect_ratio(Invader.CollideRectRatio)):
            self.set_spawn_coords(radius=Invader.SpawnRadius)
        self.update_relative_position()
        Invader.Register.add(self)

    def __del__(self):
        Invader.Register.remove(self)

    def update(self, new_offset=None):
        # Basic movement:
        x, y = self.center_coords
        ratio = x / y
        print(x, y, ratio, 1. - ratio)
        self.rect = self.image.get_rect(center=tuple(map(sum, zip(new_offset, self.center_coords))))
