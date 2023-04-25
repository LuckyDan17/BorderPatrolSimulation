from BorderPatrolSimulation.Settings.Constants import Constants
from BorderPatrolSimulation.Entities.Entity import Entity


class CircleEntity(Entity):

    DefaultRadius = Constants["Entity"]["Circle"]["Radius"]["Default"]

    def __init__(self, relative_position=None, radius=None, speed=None, image_path=None, color=None):

        super().__init__(relative_position, speed, image_path, color)

        if radius is None:
            self._radius = CircleEntity.DefaultRadius
        else:
            # Parameters type checking:
            if not isinstance(radius, (int, float)):
                raise AttributeError("Wrong radius type!")

            # Parameters value checking:
            if radius < Constants["Entity"]["Circle"]["Radius"]["Min"] \
                    or radius > Constants["Entity"]["Circle"]["Radius"]["Max"]:
                raise AttributeError("Incorrect radius parameter!")

            # Value initialization:
            self._radius = radius

    # Numerical property

    @property
    def radius(self):
        return self._radius
