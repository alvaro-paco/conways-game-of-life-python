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
        self.__ecosystem = self.__setup(setup)

    def __str__(self):
        return_str = ""
        for row in self.__ecosystem:
            ecosystem_row = "\n"
            for cell in row:
                ecosystem_row += " " + str(cell)
            return_str += ecosystem_row
        return return_str

    def __setup(self,cells):
        ecosystem = []
        for row in range(self.y):
            grid_row = []
            for column in range(self.x):
                cell = Cell(row, column, True) if (row, column) in cells else Cell(row, column, False)
                grid_row.append(cell)
            ecosystem.append(grid_row)
        return ecosystem

    def next_generation(self):
        self.___fillLife();

    def __draw(self):
        grid = [['o' for y in range(self.y)]for x in range(self.x)]
        return grid

    def __addCellToEcosystem(self, cell):
        self.__ecosystem[cell.x][cell.y].setLife(True)

    def __removeCellFromEcosystem(self, cell):
        self.__ecosystem[cell.x][cell.y].setLife(False)

    def __killCells(self, cells):
        for cell in cells:
            self.__removeCellFromEcosystem(cell)

    def __reviveCells(self, cells):
        for cell in cells:
            self.__addCellToEcosystem(cell)

    def ___fillLife(self):
        """Advance the board one step and return it."""
        new_board = []
        die = []
        live = []
        for row in self.__ecosystem:
            board_row = []
            for cell in row:
                cell_live_neighbors = cell.getNeighbors(
                    ecosystem=self.__ecosystem,
                    width=self.x, height=self.y)
                # Any live cell with less than two
                # neighbors die
                if cell.live:
                    if 2 > len(cell_live_neighbors) or len(cell_live_neighbors) > 3:
                        die.append(cell)
                if not cell.live and len(cell_live_neighbors) == 3:
                    live.append(cell)
                board_row.append(cell)
            new_board.append(board_row)
        self.__killCells(die)
        self.__reviveCells(live)
        self.__ecosystem = new_board
