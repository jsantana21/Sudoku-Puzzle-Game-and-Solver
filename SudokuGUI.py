import pygame # Need to have pygame installed on your system prior to running this code
from SudokuPuzzleSolver import puzzleSolver, followsTheRules #functions imported from the SudokuPuzzleSolver python file in the same directory
import time # to keep time of how long it takes the player to complete the puzzle
import signal # signal and sys imports are needed for the signal_handler function
import sys

# Initialize the pygame program
pygame.font.init()

# Object 1: Square Class 
# Makes up the Sudoku GameBoard
class Sqaure:
    rows, columns = 9, 9

    # The attributes of a Square instance
    def __init__(self, value, row, column, width ,height):
        self.value = value
        self.temp = 0
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.selected = False

    # Drawing in the number into the square
    def draw(self, win):
        font = pygame.font.SysFont("arial", 40)

        space = self.width / 9
        x = self.column * space
        y = self.row * space

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), 1, (128,128,128)) 
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = font.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (space/2 - text.get_width()/2), y + (space/2 - text.get_height()/2)))

        if self.selected:
            # Highlights the square of interest in blue
            pygame.draw.rect(win, (0,0,255), (x,y, space ,space), 3)

    # Set value = val
    def set(self, val):
        self.value = val
        
    # Set temp = val
    def set_temp(self, val):
        self.temp = val

# Object 2: GameBoard Class 
# Holds all the Sqaures in a row, column structure  
class GameBoard:
    # To solve another sudoku puzzle simply modify into 2D array into another solvable sudoku puzzle
    # Note that 0 = empty square in this case
    # Reference to other Sudoku puzzles ranging from easy to hard: https://www.puzzles.ca/sudoku/
    gameboard = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

    # The attributes of a GameBoard instance 
    def __init__(self, rows, columns, width, height):
        self.rows = rows
        self.columns = columns
        # List comprehension to create the GameBoard which is made of squares
        self.sqaures = [[Sqaure(self.gameboard[i][j], i, j, width, height) for j in range(columns)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        # List comprehension to update the value(number) on the model that is sent to the solver function 
        self.model = [[self.sqaures[i][j].value for j in range(self.columns)] for i in range(self.rows)]

    def place(self, val):
        # Use the update_model function to write in the updated value unto the gameboard and make it pernament
        row, column = self.selected

        # If the square is empty then its fine to write in the number 
        if self.sqaures[row][column].value == 0:
            self.sqaures[row][column].set(val)
            self.update_model()

            # If the inserted number satisfies the 3 rules and fits into the solution then return True
            if followsTheRules(self.model, val, (row,column)) and puzzleSolver(self.model):
                return True
            else: # Retract inserted number, empty sqaure, and backtrack
                self.sqaures[row][column].set(0)
                self.sqaures[row][column].set_temp(0)
                self.update_model()
                return False
            
    # Sets the temporary value for the Square Object
    def sketch(self, val):
        row, column = self.selected
        self.sqaures[row][column].set_temp(val)

    # Creates the drawn background for the Sudoku GUI
    def draw(self, win):
        # Draw Grid Lines for the Sudoku Gameboard
        space = self.width / 9
        for i in range(self.rows+1):
            #Thick black lines to divide the 9x9 grid into 3 sub grids of 3x3
            if i % 3 == 0 and i != 0:
                boldness = 4
            else:
                boldness = 1
            pygame.draw.line(win, (0,0,0), (0, i*space), (self.width, i*space), boldness)
            pygame.draw.line(win, (0, 0, 0), (i * space, 0), (i * space, self.height), boldness)

        # Draw Squares for the numbers in the Sudoku GUI
        for i in range(self.rows):
            for j in range(self.columns):
                self.sqaures[i][j].draw(win)

    # Reset all other sqaures so (row,column) can be selected
    def select(self, row, column):
        for i in range(self.rows):
            for j in range(self.columns):
                self.sqaures[i][j].selected = False

        self.sqaures[row][column].selected = True
        self.selected = (row, column)

    # Clears the selected position aka sets it to 0
    def clear(self):
        row, column = self.selected
        if self.sqaures[row][column].value == 0:
            self.sqaures[row][column].set_temp(0)

    # Allows the user to click on the position they want to fill in and return the position of the square clicked on
    def click(self, position):
        if position[0] < self.width and position[1] < self.height:
            space = self.width / 9
            x = position[0] // space
            y = position[1] // space
            return (int(y),int(x))
        else:
            return None

    # Checks to see if all sqaures are filled in 
    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.sqaures[i][j].value == 0:
                    return False
        return True

def redraw_window(win, gameboard, time):
    win.fill((255,255,255))
    # Draw the time and numbers onto the Sudoku Board in Arial font 35px
    font = pygame.font.SysFont("arial", 35)
    text = font.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(text, (540 - 300, 560))
    
    # Draw Grid and Gameboard
    gameboard.draw(win)


def format_time(secs):
    second = secs%60
    minute = secs//60
    hour = minute//60

    format = " " + str(minute) + ":" + str(second)
    return format


# In the case the player wants to cancel the file by presst Ctrl+C
# Then they have the choice to quit the game or head back to playing
def signal_handler(sig, frame):
    answer = input("Are you sure you want to quit? (y/n): ")
    if answer == "y":
        print('Game Over! Better Luck Next Time!')
        sys.exit(0)
    else:
        print('Alright then...back to the Sudoku Puzzle!')
signal.signal(signal.SIGINT, signal_handler)



# Main function that calls on both classes and their function above
def main():
    win = pygame.display.set_mode((550,600))
    pygame.display.set_caption("Sudoku Puzzle [9x9]")
    gameboard = GameBoard(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()

    # While the Sudoku game is still running
    while run:
        # Estimate of the time it took the player to complete the puzzle
        play_time = round(time.time() - start)

        # Iterate through all events to interept the player's action 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                #All of the numbers you can type into each square 1-9 
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE: # Pressing the "Del" button is supposed to erase the number you about to "Enter"
                    gameboard.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = gameboard.selected
                    if gameboard.sqaures[i][j].temp != 0:
                        if gameboard.place(gameboard.sqaures[i][j].temp):
                            print("Correct!, Keep Going!")
                        else:
                            print("Sorry, Try Again with A Different Number!")
                        key = None
                        # You completed the Sudoku puzzle correctly
                        if gameboard.is_finished():
                            print("Congratulations, You Won!!!")
                            print("Thanks for Playing!!!")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                clicked = gameboard.click(position)
                if clicked:
                    gameboard.select(clicked[0], clicked[1])
                    key = None

        if gameboard.selected and key != None:
            gameboard.sketch(key)

        redraw_window(win, gameboard, play_time)
        pygame.display.update()

main()
pygame.quit()
