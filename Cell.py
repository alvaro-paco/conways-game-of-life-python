class Cell:

    def __init__(self, x, y, live=False):
        self.x = x
        self.y = y
        self.live = live

    def __str__(self):
        return '*' if self.live else ' '

    def getPoint(self):
        return self.x, self.y

    def __neighborPosition(self, i, j, width, height):
        width, height = width - 1, height - 1

        point_x = self.x + j
        if point_x < 0:
            point_x = width
        elif point_x > width:
            point_x = 0

        point_y = self.y + j
        if point_y < 0:
            point_y = height
        elif point_y > height:
            point_y = 0

        return [point_x, point_y]

    def getNeighbors(self, ecosystem, width, height, distance=1):
        """Return the neighbors of cell."""
        r = range(0 - distance, 1 + distance)
        neighbors = []
        for i in r:
            for j in r:
                if not i == j == 0:
                    point_x, point_y = self.__neighborPosition(i, j, width, height)
                    neighbor = ecosystem[point_x][point_y]
                    if neighbor.live is True:
                        neighbors.append(neighbor)
        return neighbors

    def setLife(self, live):
        self.live = live