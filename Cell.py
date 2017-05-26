class Cell:

    def __init__(self, x, y, live=False):
        self.x = x
        self.y = y
        self.live = live

    def __str__(self):
        return '[]' if self.live else 'o'

    def getPoint(self):
        return (self.x, self.y)

    def getNeighbors(self, cell, distance=1):
        """Return the neighbors of cell."""
        r = range(0 - distance, 1 + distance)

        return (Cell(self.x + i, self.y + j, False)  # new cell offset from center
                for i in r for j in r  # iterate over range in 2d
                if not i == j == 0)  # exclude the center cell