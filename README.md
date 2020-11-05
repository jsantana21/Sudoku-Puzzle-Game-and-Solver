# Sudoku Puzzle Game & Solver

### Project Task
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A Python program that solves sudoku puzzle by using the back tracking algorithm also as a generated user interface feature where the user can play a Sudoku puzzle as the algorithm indictates to you if you're solving the puzzle correcting or not.

### Background
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Despite having a Japanese name Sudoku (数独, sūdoku) meaning single digit / number, this logic-based number puzzle was invented by retired American architect and freelance puzzle constructor Howard Garns in 1979 and would gain immense popular in Japan in the 1980's and later around the world. In this game, the goal is to fill a 9×9 grid (81 squares in total) with single digit numbers such that each column, each row, and each of the nine 3×3 subgrids that compose the gameboard / grid all have the numbers from 1 to 9. It should also be noted that the player is given a partially completed grid, which only has one single solution; the difficulty ranges from very easy to very hard depending how completed the grid when the player starts. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What makes the puzzle so challenging is that each nine-square column, nine-square row, and within each of the nine 3x3 sub sqaures, must also contain the numbers 1-9, **without repetition or omission**. Knowing how to use this constraint will help us greatly in developing the proper algorithm.

### Algorithm & Implementation
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The naive or brute force approach would be 

