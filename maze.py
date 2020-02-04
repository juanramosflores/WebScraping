import random

class Maze():
    def __init__(self,number_row, number_cols):
        self.number_row = number_row
        self.number_cols = number_cols
        self.maze_map = None

    def _create_row(self):
        map_row = [0] * self.number_row
        map = [map_row for i in range(self.number_cols)]
        return map
    
    
    
a = Maze(10,10)
print(a._create_row())
