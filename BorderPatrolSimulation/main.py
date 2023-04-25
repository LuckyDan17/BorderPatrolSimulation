from BorderPatrolSimulation.Graphics.MainWindow import MainWindow
from BorderPatrolSimulation.Settings.Constants import import_settings

if __name__ == '__main__':
    if not import_settings():
        raise ImportError("Can not import settings properly!")
    from BorderPatrolSimulation.Simulation.Simulation import Simulation
    s = Simulation()
    # main_window = MainWindow()
#
# import pygame
# import math
#
# class Circle(pygame.sprite.Sprite):
#     def __init__(self, x, y, radius, color):
#         super().__init__()
#         self.color = color
#         self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
#         pygame.draw.circle(self.image, color, (radius, radius), radius)
#         self.rect = self.image.get_rect(center=(x, y))
#
#     def area(self):
#         return math.pi * self.rect.width ** 2 / 4
#
#     def circumference(self):
#         return 2 * math.pi * self.rect.width / 2
#
# class Rectangle(pygame.sprite.Sprite):
#     def __init__(self, x, y, width, height, color):
#         super().__init__()
#         self.color = color
#         self.image = pygame.Surface((width, height), pygame.SRCALPHA)
#         self.image.fill(color)
#         self.rect = self.image.get_rect(topleft=(x, y))
#
#     def area(self):
#         return self.rect.width * self.rect.height
#
#     def perimeter(self):
#         return 2 * (self.rect.width + self.rect.height)
#
# # initialize pygame
# pygame.init()
#
# # set up the window
# size = (400, 400)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Shapes")
#
# # create a sprite group
# shapes = pygame.sprite.Group()
#
# # create an instance of each class
# my_circle = Circle(200, 200, 50, (255, 0, 0))
# my_rect = Rectangle(150, 150, 100, 50, (0, 255, 0))
#
# # add the shapes to the sprite group
# shapes.add(my_circle)
# shapes.add(my_rect)
#
# # draw the shapes
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#
#     # fill the screen with white
#     screen.fill((255, 255, 255))
#
#     # draw the shapes
#     shapes.draw(screen)
#
#     # update the screen
#     pygame.display.update()
