import random


class Grid:
    def __init__(self, possitions, mines):
        self.possitions = possitions
        self.mines = mines

    def create_grid(self):
        grid = []
        for grid_possition in range(self.possitions):
            grid.append(grid_possition)
        mines_possitions = random.sample(range(self.possitions), 10)
        play_grid = []
        for play_possition in range(self.possitions):
            if play_possition in mines_possitions:
                play_grid.append(-1)
            else:
                play_grid.append(play_possition)
        return print(play_grid)
    

print("Welcome to Minseweeper game")

Grid(100,10)