from BorderPatrolSimulation.Entities.RectangleEntities.Invader import Invader
from BorderPatrolSimulation.Entities.RectangleEntities.Sensor import Sensor
from BorderPatrolSimulation.Entities.CircleEntities.Base import Base
from BorderPatrolSimulation.Entities.Entity import Entity
import pygame


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Simulation:

    def __init__(self, window_width=700, window_height=700):

        self._width = window_width
        self._height = window_height

        pygame.init()
        self._screen = pygame.display.set_mode((self._width, self._height), pygame.RESIZABLE)
        pygame.display.set_caption("Border Patrol Simulation")
        icon = pygame.image.load("BorderPatrolSimulation/Graphics/Resources/shield-border.png")
        pygame.display.set_icon(icon)

        base = Base(color=GREEN)
        # base = Base(image_path="BorderPatrolSimulation/Graphics/Resources/base.png", color=GREEN)

        Simulation.spawn_invaders()
        Simulation.spawn_sensors()

        Entity.EntityRegister.update(self.offset)
        self._clock = pygame.time.Clock()

        while base.is_alive:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    self._width, self._height = event.size
                    if self._width < 500:
                        self._width = 500
                    if self._height < 500:
                        self._height = 500
                    self._screen = pygame.display.set_mode((self._width, self._height), pygame.RESIZABLE)
                    Entity.EntityRegister.update(new_offset=self.offset)

            self._background = pygame.Surface(self._screen.get_size())
            self._background.fill((255, 255, 255))
            self._screen.blit(self._background, (0, 0))
            Entity.EntityRegister.clear(self._screen, self._background)

            Entity.EntityRegister.update(self.offset)

            Entity.EntityRegister.draw(self._screen)

            pygame.display.flip()
            self._clock.tick(60)

    @property
    def offset(self):
        x, y = self._screen.get_size()
        return x // 2, y // 2

    @staticmethod
    def spawn_invaders():
        for i in range(10):
            Invader(color=BLUE)

    @staticmethod
    def spawn_sensors():
        for i in range(10):
            Sensor(color=RED)

# b = Base()

# # Define some colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
#
# # Define the border dimensions
# BORDER_WIDTH = 10
# BORDER_HEIGHT = 10
#
# # Create a sprite class for the border
# class Border(pygame.sprite.Sprite):
#     def __init__(self, x, y, width, height, color):
#         super().__init__()
#         self.image = pygame.Surface([width, height])
#         self.image.fill(color)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#
# # Create a sprite class for the border patrol agents
# class Agent(pygame.sprite.Sprite):
#     def __init__(self, x, y, color):
#         super().__init__()
#         self.image = pygame.Surface([10, 10])
#         self.image.fill(color)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.direction = random.choice(['up', 'down', 'left', 'right'])
#
#     def update(self):
#         if self.direction == 'up':
#             self.rect.y -= 1
#         elif self.direction == 'down':
#             self.rect.y += 1
#         elif self.direction == 'left':
#             self.rect.x -= 1
#         elif self.direction == 'right':
#             self.rect.x += 1
#
#         if self.rect.y <= BORDER_HEIGHT:
#             self.direction = 'down'
#         elif self.rect.y >= HEIGHT - BORDER_HEIGHT - 10:
#             self.direction = 'up'
#         elif self.rect.x <= BORDER_WIDTH:
#             self.direction = 'right'
#         elif self.rect.x >= WIDTH - BORDER_WIDTH - 10:
#             self.direction = 'left'
#
# # Create a sprite group for the border patrol agents
# agent_group = pygame.sprite.Group()
#
# # Create a sprite group for the border
# border_group = pygame.sprite.Group()
#
# # Create the top border
# border_top = Border(0, 0, WIDTH, BORDER_HEIGHT, WHITE)
# border_group.add(border_top)
#
# # Create the bottom border
# border_bottom = Border(0, HEIGHT - BORDER_HEIGHT, WIDTH, BORDER_HEIGHT, WHITE)
# border_group.add(border_bottom)
#
# # Create the left border
# border_left = Border(0, BORDER_HEIGHT, BORDER_WIDTH, HEIGHT - 2 * BORDER_HEIGHT, WHITE)
# border_group.add(border_left)
#
# # Create the right border
# border_right = Border(WIDTH - BORDER_WIDTH, BORDER_HEIGHT, BORDER_WIDTH, HEIGHT - 2 * BORDER_HEIGHT, WHITE)
# border_group.add(border_right)
#
# # Create some agents and add them to the agent group
# for i in range(10):
#     agent = Agent(random.randint(BORDER_WIDTH + 10, WIDTH - BORDER_WIDTH - 20),
#                   random.randint(BORDER_HEIGHT + 10, HEIGHT - BORDER_HEIGHT - 20),
#                   GREEN)
#     agent_group.add(agent)
#
# # Set the clock for the game
# clock = pygame.time.Clock()
#
# # Run the game loop
# running = True
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Update the agents
#     agent_group.update()
#
#     # Check for collisions between agents and border
#     collisions = pygame.sprite.groupcollide(agent_group, border_group, False, False)
#
#     # For each collision, reverse the direction of the agent
#     for agent in collisions.keys():
#         agent.direction = random.choice(['up', 'down', 'left', 'right'])
#
#     # Fill the background with black
#     screen.fill(BLACK)
#
#     # Draw the border and agents
#     border_group.draw(screen)
#     agent_group.draw(screen)
#
#     # Update the display
#     pygame.display.flip()
#
#     # Set the framerate
#     clock.tick(60)


