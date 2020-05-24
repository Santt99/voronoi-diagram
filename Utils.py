import math
from Edge import Edge
from Vertex import Vertex


def CircleIntersection(c1, c2):
    c1_origin = c1.origin_point
    c2_origin = c2.origin_point

    centerdx = c1_origin.x - c2_origin.x
    centerdy = c1_origin.y - c2_origin.y
    R = math.sqrt(centerdx ** 2 + centerdy ** 2)

    if not ((abs(c1.radius - c2.radius) <= R) and (R <= c1.radius + c2.radius)):
        return None

    # intersection(s) should exist

    R2 = R * R
    R4 = c2.radius ** 2
    a = (c1.radius ** 2 - c2.radius ** 2) / (2 * R2)
    r2r2 = c1.radius ** 2 - c2.radius ** 2
    c = math.sqrt(2 * (c1.radius ** 2 + c2.radius ** 2) /
                  R2 - (r2r2 * r2r2) / R4 - 1)

    fx = (c1_origin.x + c2_origin.x) / 2 + a * (c2_origin.x - c1_origin.x)
    gx = c * (c2_origin.y - c1_origin.y) / 2
    ix1 = fx + gx
    ix2 = fx - gx

    fy = (c1_origin.y + c2_origin.y) / 2 + a * (c2_origin.y - c1_origin.y)
    gy = c * (c1_origin.x - c2_origin.x) / 2
    iy1 = fy + gy
    iy2 = fy - gy

    return Edge(from_point=Vertex(int(ix1), int(iy1)), to_point=Vertex(int(ix2), int(iy2)))
