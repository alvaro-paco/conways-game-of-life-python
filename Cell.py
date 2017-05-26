class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.death = True

    def __str__(self):
        return '.' if self.death else '[]'