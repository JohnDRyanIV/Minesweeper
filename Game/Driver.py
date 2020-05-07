from Board import MineBoard as mb
import tkinter as tk
from tkinter import font


# Calculates what tiles the move uncovers and adjusts buttons accordingly
def updateBoard(row, col):
    # Disables all buttons on the board and brings up a window informing you that you've lost
    def showLose():
        board.uncoverAllMines()
        for r in range(board.num_rows):
            for c in range(board.num_cols):
                buttons[r][c]["state"] = ["disabled"]
        lose = tk.Tk()
        lose.title("Game Lost")
        lose_text = tk.Label(lose, text="You lost! Better luck next time!").grid(row=0, column=0)
        lose.mainloop()

    # Disables all buttons on the board and brings up a window informing you that you've won
    def showWin():
        for r in range(board.num_rows):
            for c in range(board.num_cols):
                buttons[r][c]["state"] = ["disabled"]
        win = tk.Tk()
        win.title("Congratulations!")
        win_text = tk.Label(win, text="You've won! You're the winner!").grid(row=0, column=0)
        win.mainloop()

    if board.isCovered(row, col) and var_flag.get() == 0:
        board.processMove(row, col)  # Processes the move on that location of the board
    elif var_flag.get() == 1:  # Places or removes a flag on given location
        if board.hasFlag(row, col):
            board.removeFlag(row, col)
        elif board.getNumFlags() == board.num_mines: # Every mine should be covered if this many flags have been placed,
                                                     # therefore no more flags can be placed
            pass
        else:
            board.addFlag(row, col)
    # board.showBoard()  # Debugging purposes, ensuring consistency between board lists and button displays
    # Updating button states to reflect board and ensuring everything is properly colored
    for r in range(board.num_rows):
        for c in range(board.num_cols):
            # Decide color things up here
            if board.tile_state[r][c] == 1:
                buttons[r][c]["state"] = ["disabled"]
                if board.tile_content[r][c] == 9:
                    buttons[r][c].config(background="red")
                else:
                    buttons[r][c].config(background=background_colors[color + 1], foreground=text_colors[color])
            else:
                buttons[r][c].config(background=background_colors[color], foreground=text_colors[color])
            buttons[r][c].config(text=board.getCurrentShownText(r, c))

    if board.attempts < 1:  # If all attempts have been used up without uncovering all mines, show lose screen
        showLose()
    elif board.getSquaresUncovered() - board.getMinesUncovered() + board.getMinesPlaced() == board.num_tiles:
        # If all spaces not containing mines have been uncovered without using up all attempts, show win screen
        showWin()

    print(str(board.boardInfo()))
    # var_mines.set("Mines remaining: " + str(board.num_mines - board.getMinesUncovered - board.getNumFlags()))


# Saves the board layout to a file
def saveGame():
    board.saveGame()


# Loads the board layout from a file
def loadGame():
    # Method returns false if board incompatible, loads the board successfully otherwise.
    if board.loadGame() == False:
        print("You can't load a game with a different number of rows and columns to the current one!")
    else:
        for r in range(board.num_rows):
            for c in range(board.num_cols):
                # Decide color things up here
                if board.tile_state[r][c] == 1:
                    buttons[r][c]["state"] = ["disabled"]
                    buttons[r][c].config(background=background_colors[color + 1], text=text_colors[color])
                elif board.tile_state[r][c] == 0:
                    buttons[r][c]["state"] = ["active"]
                    buttons[r][c].config(background=background_colors[color], text=text_colors[color])
                else:
                    buttons[r][c].config(background=background_colors[color], text=text_colors[color])
                buttons[r][c].config(text=board.getCurrentShownText(r, c))



"""
Easy: 10 rows, 6 columns
Medium: 15 rows, 8 columns
Hard: 20 rows, 10 columns
"""

# Driver

m = tk.Tk()
text = tk.Text(m)
myFont = font.Font(family="Courier New", size=12)
text.configure(font=myFont)

buttons = [[]]

valid_input = False

color = ''
difficulty = ''
size = ''
attempts = ''

# Obtaining user input for color scheme
while not valid_input:
    valid_colors = ["blue", "green", "brown"]
    color = input("What color do you want (blue, green, brown)?: ").lower()
    if color in valid_colors:
        valid_input = True
    else:
        print("Invalid input! Enter again.")
valid_input = False

# Obtaining user input for difficulty
while not valid_input:
    valid_difficulty = ["easy", "medium", "hard", 'e', 'm', 'h']
    difficulty = input("What difficulty would you like to play at (easy, medium, hard)?: ").lower()
    if difficulty in valid_difficulty:
        valid_input = True
    else:
        print("Invalid input! Enter again.")
valid_input = False

# Obtaining user input for board size
while not valid_input:
    valid_size = ['small', 'medium', 'large', 's','m','l']
    size = input("What size would you like the board to be (small, medium, large)?: ").lower()
    if size in valid_size:
        valid_input = True
    else:
        print("Invalid input! Enter again.")
valid_input = False

# Obtaining user input for attempt number
while not valid_input:
    valid_attempts = ['1', '2', '3', '4', '5']
    attempts = str(input("How many attempts would you like to have (1-5)?: "))
    if attempts in valid_attempts:
        valid_input = True
    else:
        print("Invalid input! Enter again.")

if difficulty == 'easy' or difficulty == 'e':
    difficulty = 1
elif difficulty == 'medium' or difficulty == 'm':
    difficulty = 2
else:
    difficulty = 3

if size == 'small' or size == 's':
    size = 1
elif size == 'medium' or size == 'm':
    size = 2
else:
    size = 3

print("Difficulty: " + str(difficulty) + " | Size: " + str(size))

attempts = int(attempts)


    

# Initializes buttons array for easy game
if size == 1:
    board = mb.MineBoard(10, 6, difficulty, attempts)
    buttons = [[tk.Button(m, text=" ", command=lambda: updateBoard(0, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 5))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(1, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 5))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(2, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 5))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(3, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 5))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(4, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 5))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(5, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 5))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(6, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 5))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(7, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 5))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(8, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 5))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(9, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 5))]]
    for r in range(board.num_rows):
        for c in range(board.num_cols):
            buttons[r][c].grid(row=r, column=c, sticky="ew")

# Initializes buttons array for medium difficulty game
elif size == 2:
    board = mb.MineBoard(15, 8, difficulty, attempts)
    buttons = [[tk.Button(m, text=" ", command=lambda: updateBoard(0, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(1, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(2, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(3, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(4, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(5, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(6, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(7, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(8, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(9, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(10, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(11, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(12, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(13, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 7))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(14, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 7))]]
    for r in range(board.num_rows):
        for c in range(board.num_cols):
            buttons[r][c].grid(row=r, column=c, sticky="ew")

# Initializes buttons array for hard game.
else:
    board = mb.MineBoard(20, 10, difficulty, attempts)
    buttons = [[tk.Button(m, text=" ", command=lambda: updateBoard(0, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 7)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 8)), tk.Button(m, text=" ", command=lambda: updateBoard(0, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(1, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 7)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 8)), tk.Button(m, text=" ", command=lambda: updateBoard(1, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(2, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 7)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 8)), tk.Button(m, text=" ", command=lambda: updateBoard(2, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(3, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 7)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 8)), tk.Button(m, text=" ", command=lambda: updateBoard(3, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(4, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 7)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 8)), tk.Button(m, text=" ", command=lambda: updateBoard(4, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(5, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 7)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 8)), tk.Button(m, text=" ", command=lambda: updateBoard(5, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(6, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 7)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 8)), tk.Button(m, text=" ", command=lambda: updateBoard(6, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(7, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 7)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 8)), tk.Button(m, text=" ", command=lambda: updateBoard(7, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(8, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 7)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 8)), tk.Button(m, text=" ", command=lambda: updateBoard(8, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(9, 0)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 1)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 2)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 3)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 4)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 5)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 6)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 7)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 8)), tk.Button(m, text=" ", command=lambda: updateBoard(9, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(10, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 7)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 8)),tk.Button(m, text=" ", command=lambda: updateBoard(10, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(11, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 7)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 8)),tk.Button(m, text=" ", command=lambda: updateBoard(11, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(12, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 7)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 8)),tk.Button(m, text=" ", command=lambda: updateBoard(12, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(13, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 7)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 8)),tk.Button(m, text=" ", command=lambda: updateBoard(13, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(14, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 7)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 8)),tk.Button(m, text=" ", command=lambda: updateBoard(14, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(15, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(15, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(15, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(15, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(15, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(15, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(15, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(15, 7)),tk.Button(m, text=" ", command=lambda: updateBoard(15, 8)),tk.Button(m, text=" ", command=lambda: updateBoard(15, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(16, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(16, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(16, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(16, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(16, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(16, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(16, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(16, 7)),tk.Button(m, text=" ", command=lambda: updateBoard(16, 8)),tk.Button(m, text=" ", command=lambda: updateBoard(16, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(17, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(17, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(17, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(17, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(17, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(17, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(17, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(17, 7)),tk.Button(m, text=" ", command=lambda: updateBoard(17, 8)),tk.Button(m, text=" ", command=lambda: updateBoard(17, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(18, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(18, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(18, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(18, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(18, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(18, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(18, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(18, 7)),tk.Button(m, text=" ", command=lambda: updateBoard(18, 8)),tk.Button(m, text=" ", command=lambda: updateBoard(18, 9))],
               [tk.Button(m, text=" ", command=lambda: updateBoard(19, 0)),tk.Button(m, text=" ", command=lambda: updateBoard(19, 1)),tk.Button(m, text=" ", command=lambda: updateBoard(19, 2)),tk.Button(m, text=" ", command=lambda: updateBoard(19, 3)),tk.Button(m, text=" ", command=lambda: updateBoard(19, 4)),tk.Button(m, text=" ", command=lambda: updateBoard(19, 5)),tk.Button(m, text=" ", command=lambda: updateBoard(19, 6)),tk.Button(m, text=" ", command=lambda: updateBoard(19, 7)),tk.Button(m, text=" ", command=lambda: updateBoard(19, 8)),tk.Button(m, text=" ", command=lambda: updateBoard(19, 9))]]
    for r in range(board.num_rows):
        for c in range(board.num_cols):
            buttons[r][c].grid(row=r, column=c, sticky="ew")

background_colors = ["sky blue", "deep sky blue", "dark khaki", "khaki", "red3", "red2"]
text_colors = ["gray1", "gray1", "azure", "azure", "white", "white"]
if color == 'blue':
    color = 0
elif color == 'green':
    color = 2
else:
    color = 3

for r in range(board.num_rows):
    for c in range(board.num_cols):
        buttons[r][c].config(background=background_colors[color])

var_mines = tk.StringVar()
var_mines.set("Num Mines: " + str(board.getMinesPlaced()))
mines_remaining = tk.Label(m, textvariable=var_mines).grid(row=board.num_rows - 1, column=board.num_cols)
var_flag = tk.IntVar()
place_flags = tk.Checkbutton(m, text="Place flags", variable=var_flag).grid(row=board.num_rows, column=board.num_cols)
btn_save = tk.Button(m, text="Save Game", command=lambda: saveGame()).grid(row=board.num_rows+1,column=board.num_cols+1)
btn_load = tk.Button(m, text="Load Game", command=lambda: loadGame()).grid(row=board.num_rows-1,column=board.num_cols+1)

m.title("Game")

board.saveGame()

m.mainloop()