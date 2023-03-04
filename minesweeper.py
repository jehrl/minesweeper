import random
from typing import Self


class Grid:
    def __init__(self, rows, lines, mines,):
        self.possitions = rows * lines
        self.mines = mines
        self.rows = rows
        self.lines = lines
        self.play_grid = []
        self.visual_grid = []
    def create_grid(self):
        for grid_possition in range(self.possitions):
            grid.append(grid_possition)
        mines_possitions = random.sample(range(1,(self.possitions + 1)), self.mines)
        for play_possition in range(1,(self.possitions + 1)):
            if play_possition in mines_possitions:
                self.play_grid.append("*")
            else:
                self.play_grid.append(play_possition)
        return self.play_grid
    def create_visual_grid(self):
        for cell in self.play_grid:
            if type(cell) == str:
                self.visual_grid.append(cell)
            else:
                neighbors = []
                if (cell)%self.lines == 0:
                    neighbors.append(cell-1)
                    neighbors.append(cell-self.lines)
                    neighbors.append(cell-self.lines-1)
                    neighbors.append(cell+self.lines-1)
                    neighbors.append(cell+self.lines)
                elif (cell)%(self.lines) == 1:
                    neighbors.append(cell+1)
                    neighbors.append(cell-self.lines+1)
                    neighbors.append(cell-self.lines)
                    neighbors.append(cell+self.lines+1)
                    neighbors.append(cell+self.lines)
                else:
                    neighbors = [cell+1, cell-1, cell+self.lines+1, cell+self.lines-1, cell+self.lines, cell-self.lines+1, cell-self.lines-1, cell-self.lines]
                mine_count = sum(1 for j in neighbors if j >= 0 and j < self.possitions and type(self.play_grid[j-1]) == str)
                self.visual_grid.append(mine_count)
        return self.visual_grid
class Player:
    def __init__(self, name):
        self.name = name
        self.actual_grid = []
        self.actual_visual_grid = []
        self.played_positions = []
    def player_visual_grid(self,grid, rows, lines):
        actual_line = 1
        for row in range(rows + 1):
            self.actual_visual_grid.append(row)
        for i, item in enumerate(grid):
            if i % lines == 0:
                self.actual_visual_grid.append(actual_line)
                self.actual_visual_grid.append(item)
                actual_line += 1
            else:   
                self.actual_visual_grid.append(item)
        return
        

    

print("Welcome to Minseweeper game")
player_nick = input("What's your nick?\n")
actual_player = Player(player_nick)
print("How big grid you wanna create?\n")
rows = int(input("How many rows:\n"))
lines = int(input("How many lines:\n"))
mines = int(input("With how many mines:\n"))
player_possition = 0
my_grid = Grid(rows,lines,mines)
my_grid.create_grid()
my_grid.create_visual_grid()
actual_player.player_visual_grid(my_grid.visual_grid,my_grid.rows, my_grid.lines)
print(actual_player.actual_visual_grid)

print("What possition you want to sweep?")
inputed_row = int(input("Enter row"))
inputed_line = int(input("Enter line"))
def neighbour(inputed_possition,grid):
        final_neigbours = []
        neighbors = []
        possitions.append(inputed_possition)
        possitions = []
        for possition in possitions
            if possition%lines == 0:
                    neighbors.append(possition-1)
                    neighbors.append(possition-lines)
                    neighbors.append(possition-lines-1)
                    neighbors.append(possition+lines-1)
                    neighbors.append(possition+lines)
                elif possition%lines == 1:
                    neighbors.append(possition+1)
                    neighbors.append(possition-lines+1)
                    neighbors.append(possition-lines)
                    neighbors.append(possition+lines+1)
                    neighbors.append(possition+lines)
                else:
                    neighbors = [possition+1, possition-1, possition+lines+1, possition+lines-1, possition+lines, possition-lines+1, possition-lines-1, possition-lines]                
            for neighbor in neighbors:
                if grid[neighbor] == 0:
                    final_neigbours.append(neighbor)
                    possitions.append(neighbor)
                    neighbour()
                elif 0 not in neighbors:
                    return 
                    
                    



def input_verification(inputed_row, inputed_line, grid, rows, lines)
    possition_index = ((inputed_line - 1) * rows) + inputed_row - (rows+1) - inputed_line - 1
    possition_value = grid[possition_index]
    if type(possition_value) == str:
        actual_player.played_positions.append(possition_index)
        grid_print()
        print("You blasted mine! Game over")
    elif grid[possition_value] = 0:
        final_neighbors = []
        revealed = []
        revealed.append(possition_index)
        for possition in revealed:
            final_neighbors.append(possition)
            revealed.pop(0)
            neighbors = []
            if possition % lines == 0:
                neighbors = [possition - 1, possition - lines, possition - lines - 1, possition + lines - 1, possition + lines]
            elif possition % lines == 1:
                neighbors = [possition + 1, possition - lines + 1, possition - lines, possition + lines + 1, possition + lines]
            else:
                neighbors = [possition + 1, possition - 1, possition + lines + 1, possition + lines - 1, possition + lines, possition - lines + 1, possition - lines - 1, possition - lines]
            for neighbor in neighbors:
                if grid[neighbor] == 0:
                    final_neighbors.append(neighbor)
                    revealed.append(neighbor)
        return final_neighbors