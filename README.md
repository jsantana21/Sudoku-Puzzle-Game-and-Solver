# Sudoku Puzzle Game & Solver 

### Project Duraiton: October 14, 2020 - November 4, 2020

### Project Task
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A Python program that solves sudoku puzzle by using the back tracking algorithm also as a generated user interface feature where the user can play a Sudoku puzzle as the algorithm indictates to you if you're solving the puzzle correcting or not.

### Background
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Despite having a Japanese name Sudoku (数独, sūdoku) meaning single digit / number, this logic-based number puzzle was invented by retired American architect and freelance puzzle constructor Howard Garns in 1979 and would gain immense popular in Japan in the 1980's and later around the world. In this game, the goal is to fill a 9×9 grid (81 squares in total) with single digit numbers such that each column, each row, and each of the nine 3×3 subgrids that compose the gameboard / grid all have the numbers from 1 to 9. It should also be noted that the player is given a partially completed grid, which only has one single solution; the difficulty ranges from very easy to very hard depending how completed the grid when the player starts. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What makes the puzzle so challenging is that each nine-square column, nine-square row, and within each of the nine 3x3 sub sqaures, must also contain the numbers 1-9, **without repetition or omission**. Knowing how to use this constraint will help us greatly in developing the proper algorithm.

### Algorithm & Implementation
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The naive or brute force approach to solving a Sudoku would be to go through with every single combination of numbers for each sqaure in the grid. Though it will give us the solution to the puzzle, the algorithm is extremely slow as there are 81 squares in the grid each of them having 9 different possibilites. Meaning that the time complexity of this brute force algorithm is expoential as it would go through 9<sup>81</sup> different combination to find the solution. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The most optimal approach to solving this problem would be to use the back tracking algorithm where it does the following while iterating through each square row by row:
1. Find and pick an empty square in the Sudoku grid / gameboard
1. Try all single digit combination (numbers 1-9)
1. Find one number that works and satisifes the game rules
1. Repeat step 3 
1. If the solution can't be found, then backtrack \

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What its essentially trying to do is to solve each sqaure at a time and recursively check to see if the solution works until it eventually gets the one solution. So rather than continuing a solution that works, like the naive approach, the backtracking approach only continue the solution that does work and solves the puzzle. If the solution doesn't work, then it backtrack and tries a different number to see if the solution works.

### Results
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In the sudokuPuzzleSolver.py file, the code on how to solve a 9x9 Sudoku puzzle by the use of backtracking is found here. It has a function to find the empty squares in the grid (which is denoted by 0), another function to check that all three rules of Sudoku are being met (each nine-square column, nine-square row, and within each of the nine 3x3 sub sqaures, must also contain the numbers 1-9, **without repetition or omission**), and the recursive puzzle solver function which incorpates the previous two functions to solve the puzzle. It also has a function to print out the board in string form and a test case to make that it solves the puzzle correctly. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The SudokuGUI.py file incorporates the functions from the first file along with the importing of the pygame module to create the GUI by making the Gameboard Object that has functions to allow the user to click the sqaure into the grid, draw on the grid to insert the number of their choice. It also has a Square Object class with functions that to define the boundaries of the squares so the program what the user can click on. The program also gives the user feedback as whether they chose the right number or not. For more details check the comments in the py files. \ 

| <img src="https://github.com/jsantana21/Sudoku-Puzzle-Game-and-Solver/blob/main/images/Sudoku%20Puzzle%20GUI.png" width="450" height="450" />      | <img src="https://github.com/jsantana21/Sudoku-Puzzle-Game-and-Solver/blob/main/images/Sudoku%20Puzzle%20Terminal%20Messages.png" width="450" height="450" /> |



### What Could be Improved?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; I was unfornately unable to get the 'Del' key option to work where the user could be able to delete a number from an empty sqaure. The user however could replace one number with another number key option so I figured that not having a'Del' One immediate thing that comes to mind that I can improve in this project to generate solvable 9x9 Sudoku puzzles instead of the user having to look up Sudoku puzzles online and manullay edit the 2D array in the files. Trying to code out this feature would be a whole endeavor in itself potentailly making this project a full blown web app where I would have to a database in the backend of 9x9 Sudoku puzzles I would get from online. Maybe someday I will return back to this project to add this feature and more such as a online multiplayer feature. 
