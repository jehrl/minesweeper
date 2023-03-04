import random
import time

class Grid:
    def __init__(self, rows, lines, mines,):
        self.possitions = rows * lines
        self.mines = mines
        self.rows = rows
        self.lines = lines
        self.play_grid = []
        self.visual_grid = []
    def create_grid(self):
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
    def player_actual_grid(self, grid):
        for item in grid:
            self.actual_grid.append(item)
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
actual_player.player_actual_grid(my_grid.visual_grid)
print(actual_player.actual_grid)

print("What possition you want to sweep?")
inputed_row = int(input("Enter row"))
inputed_line = int(input("Enter line"))
def input_verification(inputed_row, inputed_line, grid, rows, lines):
    possition_index = (((inputed_line - 1) * rows) + inputed_row - 1)
    possition_value = grid[possition_index]
    print(possition_index)
    print(possition_value)
    if type(possition_value) == str:
        actual_player.played_positions.append(possition_index)
        print("You blasted mine! Game over")
    elif grid[possition_index] == 0:
        final_neighbors = []
        revealed = []
        revealed.append(possition_index)
        while revealed:
            print("revealed " + str(revealed))
            possition = revealed.pop(0)
            print("reveal" + str(possition))
            neighbors = []
            clear_neighbors = []
            print("possition" + str(possition))
            if possition % lines + 1 == 0:
                neighbors = [possition - 1, possition - lines, possition - lines - 1, possition + lines - 1, possition + lines]
            elif possition % lines + 1 == 1:
                neighbors = [possition + 1, possition - lines + 1, possition - lines, possition + lines + 1, possition + lines]
            else:
                neighbors = [possition + 1, possition - 1, possition + lines + 1, possition + lines - 1, possition + lines, possition - lines + 1, possition - lines - 1, possition - lines]
            for clear_neighbor in neighbors:
                if clear_neighbor < len(grid) and clear_neighbor >= 0:
                    clear_neighbors.append(clear_neighbor)
            print(clear_neighbors)
            for neighbor in clear_neighbors:
                if grid[neighbor] == 0 and neighbor not in final_neighbors:
                    final_neighbors.append(neighbor)
                    time.sleep(1)
                    revealed.append(neighbor)
        return final_neighbors

input_verification(inputed_row,inputed_line,my_grid.visual_grid,my_grid.rows,my_grid.lines)
def updating_visual_grid(zeros, )