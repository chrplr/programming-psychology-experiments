#! /usr/bin/env python
"""
Kinematogram stimuli
"""

import pygame  
import  random
import argparse

from math import cos, sin, pi

W, H = 400, 400  
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
POINT_R = 1 # each point size
DIST = 4 # inter-frame point distance 

def rand_max(max):
    return max * random.random()

def rand_dirn():
    return 2 * pi * random.random()

def init_points(n, p):
    n_same_dirn = int(p * n)
    dir = rand_dirn()
    points = [(rand_max(W), rand_max(H), dir) for _ in range(n_same_dirn)]
    points.extend([(rand_max(W), rand_max(H), rand_dirn()) for _ in range(n - n_same_dirn + 1)]) 
    return points

def draw_white_point(screen, x, y):
    pygame.draw.circle(screen, WHITE, (x, y), POINT_R, 0)

def draw_points(screen, points):
    for i, (x, y, dir) in enumerate(points):
        x = (x + DIST * cos(dir)) % W
        y = (y + DIST * sin(dir)) % H
        points[i] = x, y, dir
        draw_white_point(screen, x, y)
    return points

def main():
    parser = argparse.ArgumentParser(prog='Kinematogram Stimulus', description='Kinematogram stimulus drawing')
    parser.add_argument('-n', '--n-points', default=500, type=int)
    parser.add_argument('-p', '--same-direction-proportion', default=0.4, type=float,
                        help="Proportion of points moving in the same direction, in the range of 0 to 1")
    args = parser.parse_args()

    N_POINTS = args.n_points
    P = args.same_direction_proportion

    pygame.init()
    screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
    pygame.display.set_caption('Kinematogram stimulus')
    clock = pygame.time.Clock()
    fps = 20 

    points = init_points(N_POINTS, P)

    quit = False
    while not quit:
        screen.fill(BLACK)
        points = draw_points(screen, points)
        pygame.display.flip()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                continue

if __name__ == "__main__":
    main()