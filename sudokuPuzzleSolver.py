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

def print_game_board(gameboard):
    for i in range(len(gameboard)):
        # Prints out this dashed line border every 3 rows
        if i % 3 == 0 and i != 0: # i!=0 is so that a border isn't printed before row 0 
            print("- - - - - - - - - - - - - ")
        
        # Prints out this dashed line border every 3 columns
        for j in range(len(gameboard[0])):
            if j % 3 == 0 and j != 0: # j!=0 is so that a border isn't printed before col 0 
                print(" | ", end="") # end="" to prevent \n from being printed out 
            
            # Check to see if it's at the last column so it can iterate to the next row
            if j == 8:
                print(gameboard[i][j])
            else:
                print(str(gameboard[i][j]) + " ", end="")

# Test Case 
# print_game_board(gameboard)

def find_empty_sqaure(gameboard):
    for i in range(len(gameboard)):
        for j in range(len(gameboard[0])):
            if gameboard[i][j] == 0: # In our case, 0 = empty square
                return (i, j)  # Return (row,col) coordinate of empty square
    return None

# This function checks if the current gameboard is valid and abides by Sudoku's rules
def followsTheRules(gameboard, number, position):

    # Rule 1: Check each row to see if number only appears once in the row it was inserted in
    for i in range(len(gameboard[0])):
        if gameboard[position[0]][i] == number and position[1] != i: #Doesn't check position[1] since that position is where we inserted our number
            return False

    # Rule 2: Check each column to see if number only appears once in the column it was inserted in
    for i in range(len(gameboard)):
        if gameboard[i][position[1]] == number and position[0] != i: #Doesn't check position[0] since that position is where we inserted our number
            return False

    x_axis = position[1] // 3
    y_axis = position[0] // 3

    # Rule 3: Check each 3x3 box to see if number only appears once in the 3x3 it was inserted in
    for i in range(y_axis*3, y_axis*3 + 3): # To ensure it iterates through all rows in the 3x3 square
        for j in range(x_axis * 3, x_axis*3 + 3): # To ensure it iterates through all columns in the 3x3 square
            if gameboard[i][j] == number and (i,j) != position:
                return False

    return True #All 3 rules are satisified 

def puzzleSolver(gameboard): #Recursion Function

    # print(gameboard) #use to see how the function backtracked in its iterations  

    # Base Case: The gameboard is completed and a solution is found
    if not find_empty_sqaure(gameboard):
        return True
    
    # Recursive Case: A empty square is found so now it looks for a solution
    else:
        row, col = find_empty_sqaure(gameboard)

    # Check numbers 1-9 to see if it fits the solution
    for i in range(1, 10):
        if followsTheRules(gameboard, i, (row, col)): # i = number , (row, col) = position
            gameboard[row][col] = i # The number i satisfies all 3 rules and is inserted in the board

            # It recursively calls itself to see if he inserted number works in the solution
            if puzzleSolver(gameboard):
                return True
            
            #Otherwise, retract the inserted number and leave it empty/blank aka put 0 and start backtracking
            gameboard[row][col] = 0

    return False #the puzzle can't be solved in this case if a solution isn't found in the for-loop above

'''
# Test Case
print("_________________________UNSOLVED SUDOKU PUZZLE_______________________________")
print_game_board(gameboard)
puzzleSolver(gameboard)
print("_________________________THE SOLUTION_______________________________")
print_game_board(gameboard)
'''