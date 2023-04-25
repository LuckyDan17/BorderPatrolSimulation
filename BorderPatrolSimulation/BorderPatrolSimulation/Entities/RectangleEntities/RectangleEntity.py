from BorderPatrolSimulation.Settings.Constants import Constants
from BorderPatrolSimulation.Entities.Entity import Entity


class RectangleEntity(Entity):

    DefaultSize = Constants["Entity"]["Rectangle"]["Size"]["Default"]

    def __init__(self, relative_position=None, size=None, speed=None, image_path=None, color=None):

        super().__init__(relative_position, speed, image_path, color)

        # Parameters type and value checking, and value checking:
        if size is None:
            self._size = (RectangleEntity.DefaultSize[0],
                          RectangleEntity.DefaultSize[1],
                          RectangleEntity.DefaultSize[2])
        else:
            if isinstance(size, (tuple, list)):
                for i in range(len(size)):
                    if not isinstance(size[i], (int, float)):
                        raise AttributeError("Wrong size type!")
                    if size[i] < Constants["Entity"]["Rectangle"]["Size"]["Min"][i] \
                            or size[i] > Constants["Entity"]["Rectangle"]["Size"]["Max"][i]:
                        raise AttributeError("Incorrect size parameters!")
            elif not isinstance(size, (int, float)):
                raise AttributeError("Wrong size type!")
            else:
                if size < Constants["Entity"]["Rectangle"]["Size"]["Min"][0] \
                        or size > Constants["Entity"]["Rectangle"]["Size"]["Max"][0]:
                    raise AttributeError("Incorrect size parameters!")

            self._size = tuple(list(size) + [RectangleEntity.DefaultSize[i] for i in range(len(size), 3)])

    # Size properties:

    # on X axe
    @property
    def width(self):
        return self._size[0]

    # on Y axe
    @property
    def length(self):
        return self._size[1]

    # on Z axe
    @property
    def height(self):
        return self._size[2]
