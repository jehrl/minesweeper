import random

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
                if cell % self.lines == 0:
                    neighbors = [cell - 1, cell - lines, cell - lines - 1, cell + lines - 1, cell + lines]
                elif cell % self.lines == 1:
                    neighbors = [cell + 1, cell - lines + 1, cell - lines, cell + lines + 1, cell + lines]
                else:
                    neighbors = [cell+1, cell-1, cell+self.lines+1, cell+self.lines-1, cell+self.lines, cell-self.lines+1, cell-self.lines-1, cell-self.lines]
                mine_count = sum(1 for j in neighbors if j > 0 and j <= self.possitions and type(self.play_grid[j-1]) == str)
                self.visual_grid.append(mine_count)
                
        return self.visual_grid
class Player:
    def __init__(self, name):
        self.name = name
        self.actual_grid = []
        self.actual_visual_grid = []
        self.played_possitions = []
        self.game_over = False

    def player_visual_grid(self,grid, rows, lines):
        actual_line = 1
        visual_grid = []
        visual_grid.append(" ")
        for row in range(1,rows + 1):
            visual_grid.append(("\033[36m " +str(row)+ "\033[36m"))
        for i, item in enumerate(grid):
            if i % lines == 0:
                visual_grid.append(("\033[36m" + str(actual_line) + "\033[36m"))
                actual_line += 1
                if i in self.played_possitions:
                    if type(item) == str:
                        visual_grid.append(("\033[31m " +str(item)) + "\033[31m")
                    elif item > 0:
                        visual_grid.append(("\033[0m " +str(item)) + "\033[0m")
                    else:
                        visual_grid.append(("\033[32m " +str(item)) + "\033[32m")                
                else:
                    visual_grid.append("\033[33m[ ]\033[33m")
            elif i in self.played_possitions:
                if type(item) == str:
                        visual_grid.append(("\033[31m " +str(item)) + "\033[31m")
                elif item > 0:
                    visual_grid.append(("\033[0m " +str(item)) + "\033[0m")
                else:
                    visual_grid.append(("\033[32m " +str(item)) + "\033[32m")
            else:   
                visual_grid.append("\033[33m[ ]\033[33m")
        for i, item in enumerate(visual_grid):
            print((item), end= "\t")
            if (i+1) % (rows + 1)  == 0:
                print("\n")
        print("\n")
        return

    def player_actual_grid(self, grid):
        for item in grid:
            self.actual_grid.append(item)
        return
    


    def input_verification(self,inputed_row, inputed_line, grid, rows, lines):
        possition_index = (((inputed_line - 1) * rows) + inputed_row - 1)
        possition_value = grid[possition_index]
        if type(possition_value) == str:
            self.played_possitions.append(possition_index)
            self.player_visual_grid(grid,rows,lines)
            print("\033[31mYou blasted mine! Game over\n\033[31m")
            self.game_over = True
        elif grid[possition_index] == 0:
            revealed = []
            revealed.append(possition_index)
            while revealed:
                possition = revealed.pop(0)
                neighbors = []
                clear_neighbors = []
                if possition % lines + 1 == 0:
                    neighbors = [possition - 1, possition - lines, possition - lines - 1, possition + lines - 1, possition + lines]
                elif possition % lines + 1 == 1:
                    neighbors = [possition + 1, possition - lines + 1, possition - lines, possition + lines + 1, possition + lines]
                else:
                    neighbors = [possition + 1, possition - 1, possition + lines + 1, possition + lines - 1, possition + lines, possition - lines + 1, possition - lines - 1, possition - lines]
                for clear_neighbor in neighbors:
                    if clear_neighbor < len(grid) and clear_neighbor >= 0:
                        clear_neighbors.append(clear_neighbor)
                for neighbor in clear_neighbors:
                    if grid[neighbor] == 0 and neighbor not in self.played_possitions:
                        self.played_possitions.append(neighbor)
                        revealed.append(neighbor)
            self.player_visual_grid(grid,rows,lines)
            print("\033[0m\033[0mPossition on row "+ str(inputed_row) + " and line " + str(inputed_line) + " is : " + str(grid[possition_index])+ "\n")
        elif grid[possition_index] > 0:
            self.played_possitions.append(possition_index)
            self.player_visual_grid(grid,rows,lines)
            print("\033[0m\033[0mPossition on row "+ str(inputed_row) + " and line " + str(inputed_line) + " is : " + str(grid[possition_index])+ "\n")
        return



def updating_visual_grid(self):
    pass

    

print("Welcome to Minseweeper game")
player_nick = input("What's your nick?\n")
actual_player = Player(player_nick)
print("How big grid you wanna create?\n")
while True:
    try:
        rows = int(input("How many rows:\n"))
        break
    except ValueError:
        print("Input must be number")
while True:
    try:
        lines = int(input("How many lines:\n"))
        break
    except ValueError:
        print("Input must be number")

while True:
    try:
        mines = int(input("With how many mines:\n"))
        break
    except ValueError:
        print("Input must be number")
player_possition = 0
my_grid = Grid(rows,lines,mines)
my_grid.create_grid()
my_grid.create_visual_grid()
actual_player.player_actual_grid(my_grid.visual_grid)
actual_player.player_visual_grid(my_grid.visual_grid,my_grid.rows,my_grid.lines)
def game():
    if (len(actual_player.played_possitions) + my_grid.mines) == (len(my_grid.visual_grid)) and actual_player.game_over == False:
        return print("\n\033[35mCongatulations!!! You won!\033[35m\n")
    elif actual_player.game_over == False:
        print("\033[0m\033[0mWhat possition you want to sweep?")
        while True:
            try:
                inputed_row = int(input("Enter row\n"))
                inputed_line = int(input("Enter line\n"))
                if (((inputed_line - 1) * my_grid.rows) + inputed_row - 1) >= len(my_grid.visual_grid):
                    print("\033[0m\033[0mYou selected position out of the reach of the grid")
                    continue
                elif (((inputed_line - 1) * my_grid.rows) + inputed_row - 1) < 0:
                    print("\033[0m\033[0mYou selected position out of the reach of the grid")
                    continue
                elif (((inputed_line - 1) * my_grid.rows) + inputed_row - 1) in actual_player.played_possitions:
                    print("\033[0m\033[0mThis position has already been revealed.")
                    continue
                break
            except ValueError:
                print("Input must be number")
        print("\n")
        actual_player.input_verification(inputed_row,inputed_line,my_grid.visual_grid,my_grid.rows,my_grid.lines)
        game()
    else:
        return
game()