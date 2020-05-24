import random
from Vertex import Vertex
from Circle import Circle
import pygame
import time
import concurrent.futures
from Utils import CircleIntersection


def main():
    pygame.init()
    SCREEN_SURFACE = pygame.display.set_mode((1000, 1000))
    SCREEN_SURFACE.fill((255, 255, 255))
    pygame.display.set_caption("Voronoi Algorithm")
    points = [Vertex(random.randint(0, 1000), random.randint(0, 1000))
              for i in range(0, 10)]
    RADIUS_DELTA = 1
    current_radius = 1
    intersections = []
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # if current_radius > 1000:
        #     running = False
        SCREEN_SURFACE.fill((255, 255, 255))
        circles = [Circle(current_point, current_radius)
                   for current_point in points]
        if current_radius < 1000:
            current_radius += RADIUS_DELTA

        for current_circle in circles:

            origin_point_list = [
                current_circle.origin_point.x, current_circle.origin_point.y]
            for next_circle in circles:
                futures = []
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    futures.append(executor.submit(
                        get_inters, circles, current_circle, next_circle, intersections))

            for i in range(len(intersections)):
                pygame.draw.circle(
                    SCREEN_SURFACE, (255, 0, 0, 0), intersections[i], 5)
            for i in range(len(points)):
                pygame.draw.circle(
                    SCREEN_SURFACE, (0, 255, 0, 0), points[i].to_list(), 10)
            if current_radius < 1000:
                pygame.draw.circle(SCREEN_SURFACE, (0, 0, 0, 0),
                                   origin_point_list, current_circle.radius, 1)

            # if len(intersections) > 1:
            #     pygame.draw.lines(
            #         SCREEN_SURFACE, (255, 0, 0, 0), False, intersections, 1)
        pygame.display.flip()
        # time.sleep(.001)


def get_inters(circles, current_circle, next_circle, intersections):
    if next_circle == current_circle:
        return
    edge = CircleIntersection(current_circle, next_circle)
    if not edge:
        return
    points = [edge.from_point, edge.to_point]
    for point in points:
        isValid = True
        for circle in circles:
            if circle == current_circle or circle == next_circle:
                continue
            if circle.point_is_inside(point):
                isValid = False
        if isValid:
            intersections.append(point.to_list())


if __name__ == "__main__":
    main()
