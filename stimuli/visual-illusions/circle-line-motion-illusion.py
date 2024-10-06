#! /usr/bin/env python
# Time-stamp: <2021-02-25 21:43:23 christophe@pallier.org>
""" Illusory Line-motion demo. See <https://www.youtube.com/watch?v=hA2Ag1LGJ80>

Ref: Jancke, Dirk, Frédéric Chavane, Shmuel Naaman, and Amiram Grinvald. 2004. “Imaging Cortical Correlates of Illusion in Early Visual Cortex.” Nature 428 (6981): 423–26. https://doi.org/10.1038/nature02396.

"""

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

W, H = 800, 500  # window size
center_x = W // 2
center_y = H // 2


def ilm(direction, delay=100):
    """ Displays the illusory line motion illusion <https://www.youtube.com/watch?v=hA2Ag1LGJ80>

    Args:
        direction:    'left' or 'right'
        delay : temporal interval (in ms) between the display of the circle and segment
    """
    assert direction in ['left', 'right']

    width, height = 200, 5  # size of the horizontal line
    radius = 20

    top = H // 2 - height // 2
    left = W // 2 - width // 2  # left side of the line
    segment = pygame.Rect(left, top, width, height)

    if direction == 'right':
        circle_x = left - radius
    else:  # direction is 'left'
        circle_x = left + width + radius

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (circle_x, center_y), radius)
    pygame.display.flip()
    pygame.time.wait(delay)
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, segment)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill(WHITE)
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
    pygame.set_display('Line Motion Illusion')

    screen.fill(WHITE)

    for dir in ['left', 'left', 'left', 'right', 'right', 'right']:
        ilm(dir)
        pygame.time.wait(2000)

    pygame.quit()
