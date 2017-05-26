"""Python implementation of Conway's Game of Life
Somewhat inspired by Jack Diederich's talk `Stop Writing Classes`
http://pyvideo.org/video/880/stop-writing-classes
Ironically, as I extended the functionality of this module it seems obvious
that the next step would be to refactor board into a class with advance and
constrain as methods and print_board as __str__.
"""

import sys
import time
import pygame as pygame


GLIDER = {
    (2, 2),
    (1, 2),
    (0, 2),
    (2, 1),
    (9, 9),
    (8, 9),
    (9, 8),
    (8, 10),
    (9, 10),
    (10, 10),
    (10, 9),
    (10, 8)
}


def neighbors(cell, distance=1):
    """Return the neighbors of cell."""
    x, y = cell
    r = range(0 - distance, 1 + distance)
    return ((x + i, y + j) # new cell offset from center
            for i in r for j in r # iterate over range in 2d
            if not i == j == 0) # exclude the center cell


def fillLife(ecosystem):
    """Advance the board one step and return it."""
    new_board = []
    for cell in ecosystem:
        cell_neighbors = set(neighbors(cell))
        # test if live cell dies
        if len(ecosystem & cell_neighbors) in [2, 3]:
            print(len(ecosystem & cell_neighbors))
            new_board.append(cell)
        # test dead neighbors to see if alive
        for n in cell_neighbors:
            if len(ecosystem & set(neighbors(n))) is 3:
                new_board.append(n)
    return new_board


def constrain(board, size):
    return set(cell for cell in board if cell[0] <= size and cell[1] <= size)

def fillBoard(screen):
    w, h = screen
    rects = []
    for i in range(w):
        for j in range(h):
            rects.append((i*9.5, j*9.5, 9, 9))

    return rects


def main(ecosystem):
    pygame.init()

    DISPLAY = pygame.display.set_mode((640, 480), 0, 32)
    WHITE = (0, 0, 0)
    BOARD = (68,51)
    DISPLAY.fill(WHITE)

    for rect in fillBoard(BOARD): pygame.draw.rect(DISPLAY, (255, 255, 255), rect)

    while True:
        for event in pygame.event.get():
            for cell in fillLife(ecosystem):
                x, y = cell
                pygame.draw.rect(DISPLAY, (0, 0, 0), (x*9.5, y*9.5, 9, 9))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main(GLIDER)