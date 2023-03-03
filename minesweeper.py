import random


class Grid:
    def __init__(self, possitions, mines,):
        self.possitions = possitions
        self.mines = mines
        self.play_grid = []

    def create_grid(self):
        grid = []
        for grid_possition in range(self.possitions):
            grid.append(grid_possition)
        mines_possitions = random.sample(range(self.possitions), 10)
        for play_possition in range(self.possitions):
            if play_possition in mines_possitions:
                self.play_grid.append(-1)
            else:
                self.play_grid.append(play_possition)
        return print(self.play_grid)
    def create_visual_grid(self):
        visual_grid = []
        for i, cell in enumerate(self.play_grid):
            if cell == -1:
                visual_grid.append(cell)
            else:
                neighbors = [i-11, i-10, i-9, i+9, i+10, i+11]
                if (i+1)%10 != 0:
                    neighbors.append(i+1)
                elif (i-1)%9 != 0:
                    neighbors.append(i-1)
                elif (i+9)%10 != 0
                    neighbors.append(i+9)
                mine_count = sum(1 for j in neighbors if j >= 0 and j < self.possitions and self.play_grid[j] == -1)
                visual_grid.append(mine_count)
        print(visual_grid[0:10])
        print(visual_grid[10:20])
        print(visual_grid[20:30])
        print(visual_grid[30:40])
        print(visual_grid[40:50])
        print(visual_grid[50:60])
        print(visual_grid[60:70])
        print(visual_grid[70:80])
        print(visual_grid[80:90])
        print(visual_grid[90:100])
        print(visual_grid[40:50])
        return print(visual_grid)
def game_round(play_grid, line, row):
    next_round_grid = play_grid
    final_position = ((line - 1) * 10) + (row - 1)
    if play_grid[final_position] == -1:
        return print("Game Over")
    else:
        next_round_grid[final_position]
    

print("Welcome to Minseweeper game")

my_grid = Grid(100,10)
my_grid.create_grid()
my_grid.create_visual_grid() 
