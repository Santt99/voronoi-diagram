import math


class Circle:

    def __init__(self, origin_point, radius):
        self.origin_point = origin_point
        self.radius = int(radius)

    def point_is_inside(self, point):
        x0 = self.origin_point.x
        y0 = self.origin_point.y
        dx = absolute(point.x - x0)
        dy = absolute(point.y - y0)
        return math.sqrt(dx * dx + dy * dy) < self.radius


def absolute(x):
    if x < 0:
        return 0 - x
    else:
        return x
