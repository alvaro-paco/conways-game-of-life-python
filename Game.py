import Cell

class Game:
    """Authomaton Game-of-life implementation
    """

    def __init__(self, x, y, setup=[]):
        """__init__
            Args:
                x (int): number of lines
                y (int): number of columns
                setup(:obj:`list` of :obj:`tuples`): initial ecosystem setup
        """
        self.x = x
        self.y = y
        self.ecosystem = setup

    def __str__(self):
        pass

    def next_generation(self): pass

    def __draw(self):
        pass

    def __neighbors(self, cell, distance=1):
        """Return the neighbors of cell."""
        x, y = cell
        r = range(0 - distance, 1 + distance)
        return ((x + i, y + j)  # new cell offset from center
                for i in r for j in r  # iterate over range in 2d
                if not i == j == 0)  # exclude the center cell

    def ___fillLife(self, ecosystem):
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

    def __constrain(self, board, size):
        return set(cell for cell in board if cell[0] <= size and cell[1] <= size)

    def __fillBoard(self, screen):
        w, h = screen
        rects = []
        for i in range(w):
            for j in range(h):
                rects.append((i * 9.5, j * 9.5, 9, 9))

        return rects
