from BorderPatrolSimulation.Settings.Constants import Constants
import pygame
import random
import math
import os


class Entity(pygame.sprite.Sprite):

    EntityRegister = pygame.sprite.Group()
    EntityGroupRegister = {}
    EntityCount = 0

    DefaultPosition = Constants["Entity"]["Default"]["Speed"]["Default"]
    DefaultSpeed = Constants["Entity"]["Default"]["Position"]

    def __init__(self, relative_position=None, speed=None, image_path=None, color=None):

        super().__init__()
        self._relative_position = None
        self.relative_position = relative_position
        image = None

        # Parameters type and value checking:
        if speed is None:
            speed = Entity.DefaultSpeed
        elif not isinstance(speed, (int, float)):
            raise AttributeError("Wrong speed type!")
        elif speed < Constants["Entity"]["Default"]["Speed"]["Min"] \
                or speed > Constants["Entity"]["Default"]["Speed"]["Max"]:
            raise AttributeError("Incorrect speed parameter!")

        if not (image_path or color):
            raise AttributeError("No visualization, need image or color parameter!")

        if color is not None:
            if not isinstance(color, (tuple, list, str)):
                raise AttributeError("Wrong color parameter!")
            if isinstance(color, (tuple, list)):
                if len(color) not in [3, 4] or not all([isinstance(c, int) for c in color]):
                    raise AttributeError("Incorrect color value!")
                elif not all([0 <= c <= 255 for c in color]):
                    raise AttributeError("Incorrect color value!")

        if image_path is not None:
            if not isinstance(image_path, str):
                raise AttributeError("Wrong image_path parameter!")
            elif not os.path.isfile(image_path):
                raise AttributeError("No existing file!")
            image = pygame.image.load(image_path)

        # Value initialization:
        self._offset = None
        self._speed = speed
        self.image = image
        self.color = color
        self.rect = None

        # Entity registration:
        Entity.EntityCount += 1
        Entity.EntityRegister.add(self)
        if self.type_name in Entity.EntityGroupRegister:
            Entity.EntityGroupRegister[self.type_name].add(self)
        else:
            Entity.EntityGroupRegister[self.type_name] = pygame.sprite.Group(self)

    def __del__(self):
        Entity.EntityCount -= 1
        Entity.EntityRegister.remove(self)
        if self.type_name in Entity.EntityGroupRegister:
            if len(Entity.EntityGroupRegister[self.type_name].sprites()) > 1:
                Entity.EntityGroupRegister[self.type_name].remove(self)
            else:
                del Entity.EntityGroupRegister[self.type_name]

    def update(self, new_offset=None):
        self.rect = self.image.get_rect(center=tuple(map(sum, zip(new_offset, self.center_coords))))

    def update_relative_position(self, floating_height_change=None):
        if floating_height_change is None:
            self._relative_position = (self.rect.x, self.rect.y, self._relative_position[2])
        else:
            if not isinstance(floating_height_change, (int, float)):
                raise AttributeError("Wrong floating_height_change type!")
            self._relative_position = (self.rect.x, self.rect.y, floating_height_change)

    def set_spawn_coords(self, radius=None, min_radius=None, max_radius=None):
        # TODO: type-check ?
        r = radius if radius is not None else random.random() * (max_radius - min_radius) + min_radius
        x = random.randint(-1 * int(r), int(r))
        y = (-1) ** random.randint(0, 1) * round(math.sqrt(r ** 2 - x ** 2))
        self.rect = self.image.get_rect(center=(x, y))
        return r

    @property
    def type_name(self):
        return type(self).__name__

    @property
    def relative_position(self):
        return tuple(self._relative_position)

    @relative_position.setter
    def relative_position(self, value):
        if value is None:
            value = (Entity.DefaultPosition[0], Entity.DefaultPosition[1], Entity.DefaultPosition[2])
        elif isinstance(value, (tuple, list)):
            for pos in value:
                if not isinstance(pos, (int, float)):
                    raise AttributeError("Wrong position type!")
        elif not isinstance(value, (int, float)):
            raise AttributeError("Wrong position type!")
        self._relative_position = value

    @property
    def center_coords(self):
        return self._relative_position[0], self._relative_position[1]

    @property
    def floating_height(self):
        return self._relative_position[2]

    @property
    def is_floating(self):
        return self._relative_position[2] > 0

    @property
    def speed(self):
        return self._speed

    @property
    def visualization(self):
        return "image" if self.image else "color"
