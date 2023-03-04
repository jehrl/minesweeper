import random


class Grid:
    def __init__(self, rows, lines, mines,):
        self.possitions = rows * lines
        self.mines = mines
        self.rows = rows
        self.lines = lines
        self.play_grid = []

    def create_grid(self):
        grid = []
        for grid_possition in range(self.possitions):
            grid.append(grid_possition)
        mines_possitions = random.sample(range(1,(self.possitions + 1)), self.mines)
        for play_possition in range(1,(self.possitions + 1)):
            if play_possition in mines_possitions:
                self.play_grid.append("*")
            else:
                self.play_grid.append(play_possition)
        return print(self.play_grid)
    def create_visual_grid(self):
        visual_grid = []
        for cell in self.play_grid:
            print("\n")
            if type(cell) == str:
                visual_grid.append(cell)
                print(cell)
            else:
                neighbors = []
                if (cell)%self.lines == 0:
                    neighbors.append(cell-1)
                    neighbors.append(cell-self.lines)
                    neighbors.append(cell-self.lines-1)
                    neighbors.append(cell+self.lines-1)
                    neighbors.append(cell+self.lines)
                    print(cell)
                    print(neighbors)
                elif (cell)%(self.lines) == 1:
                    neighbors.append(cell+1)
                    neighbors.append(cell-self.lines+1)
                    neighbors.append(cell-self.lines)
                    neighbors.append(cell+self.lines+1)
                    neighbors.append(cell+self.lines)
                    print(cell)
                    print(neighbors)
                else:
                    neighbors = [cell+1, cell-1, cell+self.lines+1, cell+self.lines-1, cell+self.lines, cell-self.lines+1, cell-self.lines-1, cell-self.lines]
                    print(cell)
                    print(neighbors)                    
                mine_count = sum(1 for j in neighbors if j >= 0 and j < self.possitions and type(self.play_grid[j-1]) == str)
                print(mine_count)
                visual_grid.append(mine_count)
        return print(visual_grid)
    
def game_round(play_grid, line, row):
    next_round_grid = play_grid
    final_position = ((line - 1) * 10) + (row - 1)
    if play_grid[final_position] == -1:
        return print("Game Over")
    else:
        next_round_grid[final_position]
    

print("Welcome to Minseweeper game")

my_grid = Grid(5,5,5)
my_grid.create_grid()
my_grid.create_visual_grid() 
