from BorderPatrolSimulation.Entities.RectangleEntities.RectangleEntity import RectangleEntity
from BorderPatrolSimulation.Settings.Constants import Constants
import pygame


class Sensor(RectangleEntity):

    Register = pygame.sprite.Group()
    SensorSize = Constants["Entity"]["Sensor"]["Size"]
    MaxSpawnRadius = Constants["Entity"]["Sensor"]["MaxSpawnRadius"]
    CollideRectRatio = Constants["Entity"]["Sensor"]["CollideRectRatio"]

    def __init__(self, spawn_radius=None, size=None, speed=None, image_path=None, color=None):
        super().__init__((0, 0, 0), size if size is not None else Sensor.SensorSize, speed, image_path, color)
        self.image = pygame.Surface((self.width, self.length), pygame.SRCALPHA)
        self.image.fill(color)
        min_r = Constants["Entity"]["Base"]["Radius"] + max(self._size[:2])
        self._radius = self.set_spawn_coords(radius=spawn_radius, min_radius=min_r, max_radius=Sensor.MaxSpawnRadius)
        while pygame.sprite.spritecollide(self, Sensor.Register, False,
                                          pygame.sprite.collide_rect_ratio(Sensor.CollideRectRatio)):
            self._radius = self.set_spawn_coords(radius=spawn_radius, min_radius=min_r, max_radius=Sensor.MaxSpawnRadius)
        self.update_relative_position()
        Sensor.Register.add(self)

    def __del__(self):
        Sensor.Register.remove(self)
