import random
from Vertex import Vertex
from Circle import Circle
import pygame
import time
from Utils import CircleIntersection


def main():
    pygame.init()
    SCREEN_SURFACE = pygame.display.set_mode((1000, 1000))
    SCREEN_SURFACE.fill((255, 255, 255))
    pygame.display.set_caption("Voronoi Algorithm")
    points = [Vertex(random.randint(0, 1000), random.randint(0, 1000))
              for i in range(0, 100)]
    RADIUS_DELTA = 1
    current_radius = 1
    intersections = []
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if current_radius > 198:
            running = False
        SCREEN_SURFACE.fill((255, 255, 255))
        circles = [Circle(current_point, current_radius)
                   for current_point in points]
        current_radius += RADIUS_DELTA

        for current_circle in circles:

            origin_point_list = [
                current_circle.origin_point.x, current_circle.origin_point.y]
            for next_circle in circles:
                if next_circle == current_circle:
                    continue
                edge = CircleIntersection(current_circle, next_circle)
                if not edge:
                    continue
                edge_from_point = (edge.from_point.x, edge.from_point.y)
                edge_to_point = (edge.to_point.x, edge.to_point.y)
                for circle in circles:
                    if not circle.point_is_inside(edge.from_point):
                        intersections.append(edge_from_point)
                    if not circle.point_is_inside(edge.to_point):
                        intersections.append(edge_to_point)

            for i in range(len(intersections)):
                pygame.draw.circle(
                    SCREEN_SURFACE, (255, 0, 0, 0), intersections[i], 1)
            pygame.draw.circle(SCREEN_SURFACE, (0, 0, 0, 0),
                               origin_point_list, current_circle.radius, 1)

            # if len(intersections) > 1:
            #     pygame.draw.lines(
            #         SCREEN_SURFACE, (255, 0, 0, 0), False, intersections, 1)
        pygame.display.flip()
        # time.sleep(.001)


if __name__ == "__main__":
    main()
