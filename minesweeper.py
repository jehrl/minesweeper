import random


class Grid:
    def __init__(self, possitions, mines):
        self.possitions = possitions
        self.mines = mines

    def create_grid(self):
        print("test")
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
    def create_visual_grid(play_grid):
        visual_grid = []
        for number in play_grid:
            temp = 0
            if number == -1:
                visual_grid.append(number)
            else:
                if play_grid[number - 11] < 0 and play_grid[number - 11] == -1:
                    temp += 1
                elif play_grid[number - 10] < 0 and play_grid[number - 10] == -1:
                    temp += 1
                elif play_grid[number - 9] < 0 and play_grid[number - 9] == -1:
                    temp += 1
                elif play_grid[number - 1] < 0 and play_grid[number - 1] == -1:
                    temp += 1
                elif play_grid[number + 1] == -1:
                    temp += 1
                elif play_grid[number + 9] == -1:
                    temp += 1          
                elif play_grid[number + 10] == -1:
                    temp += 1          
                elif play_grid[number + 11] == -1:
                    temp += 1             
                else:
                    temp += 0
                visual_grid.append(temp)
        return visual_grid

def game_round(play_grid, line, row):
    next_round_grid = play_grid
    final_position = ((line - 1) * 10) + (row - 1)
    if play_grid[final_position] == -1:
        return print("Game Over")
    else:
        next_round_grid[final_position]
    

print("Welcome to Minseweeper game")

Grid(100,10).create_grid() 
