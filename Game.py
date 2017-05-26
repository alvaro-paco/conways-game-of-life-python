from Cell import Cell

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
        self.ecosystem = self.__setup(setup)

    def __str__(self):
        life = self.___fillLife()
        for row in life:
            row = ""
            for cell in row:
                row += " " + str(cell)
            print('\n', row)

    def __setup(self,cells):
        ecosystem = []
        for row in range(self.y):
            grid_row = []
            for column in range(self.x):
                cell = Cell(row, column, True) if (row, column) in cells else Cell(row, column, False)
                grid_row.append(cell)
            ecosystem.append(grid_row)
        return ecosystem

    def next_generation(self): pass

    def __draw(self):
        grid = [['o' for y in range(self.y)]for x in range(self.x)]
        return grid

    def ___fillLife(self):
        """Advance the board one step and return it."""
        new_board = []
        for cell in self.ecosystem:
            cell_neighbors = cell.getNeighbors()
            # test if live cell dies
            if len(cell_neighbors) in [2, 3]:
                new_board.append(cell)
            # test dead neighbors to see if alive
            for n in cell_neighbors:
                if len(set(n.getNeighbors())) is 3:
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
