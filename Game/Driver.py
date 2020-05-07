from Board import MineBoard as mb
import tkinter as tk
from tkinter import font


# Calculates what tiles the move uncovers and adjusts buttons accordingly
def updateBoard(row, col):

    def showLose():
        board.uncoverAllMines()
        for r in range(board.num_rows):
            for c in range(board.num_cols):
                buttons[r][c]["state"] = ["disabled"]
        lose = tk.Tk()
        lose.title("Game Lost")
        lose_text = tk.Label(lose, text="You lost! Better luck next time!").grid(row=0, column=0)
        lose.mainloop()

    def showWin():
        for r in range(board.num_rows):
            for c in range(board.num_cols):
                buttons[r][c]["state"] = ["disabled"]
        win = tk.Tk()
        win.title("Congratulations!")
        win_text = tk.Label(win, text="You've won! You're the winner!").grid(row=0, column=0)
        win.mainloop()

    if board.isCovered(row, col) and var_flag.get() == 0:
        board.processMove(row, col)
    elif var_flag.get() == 1:
        board.addFlag(row, col)
    # board.showBoard()
    for r in range(board.num_rows):
        for c in range(board.num_cols):
            # Decide color things up here
            if board.tile_state[r][c] == 1:
                buttons[r][c]["state"] = ["disabled"]
                buttons[r][c].config(background=background_colors[color+1], text=text_colors[color])
            else:
                buttons[r][c].config(background=background_colors[color], text=text_colors[color])
            buttons[r][c].config(text=board.getCurrentShownText(r, c))

    if board.attempts < 1:
        showLose()
    elif board.getSquaresUncovered() - board.getMinesUncovered() + board.getMinesPlaced() == board.num_tiles:
        showWin()
    print(str(board.attempts))
    # var_mines.set("Mines remaining: " + str(board.num_mines - board.getMinesUncovered - board.getNumFlags()))

# Saves the board layout to a file
def saveGame():
    pass

# Loads the board layout from a file
def loadGame():
    pass
"""
Easy: 10 rows, 6 columns
Medium: 15 rows, 8 columns
Hard: 20 rows, 10 columns
"""

m = tk.Tk()
"""text = tk.Text(m)
myFont = font.Font(family="Courier New", size=12)
text.configure(font=myFont)"""

difficulty = int(input("Would you like to play at difficulty level 1, 2, or 3?: "))
buttons = [[]]

# Initializes buttons array for easy game
if difficulty == 1:
    board = mb.MineBoard(10, 6, 1, 3)
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
elif difficulty == 2:
    board = mb.MineBoard(15, 8, 2, 3)
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
    board = mb.MineBoard(20, 10, 1, 3)
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
text_colors = ["Black", "black", "azure", "azure", "white", "white"]
color = int(input("Choose color scheme: Blue (1), khaki (2), or red (3): "))
if color == 1:
    color = 0
elif color == 3:
    color = 4

for r in range(board.num_rows):
    for c in range(board.num_cols):
        buttons[r][c].config(background=background_colors[color])

var_mines = tk.StringVar()
var_mines.set(str(board.getMinesPlaced()))
mines_remaining = tk.Label(m, textvariable=var_mines).grid(row=board.num_rows - 1, column=board.num_cols)
var_flag = tk.IntVar()
place_flags = tk.Checkbutton(m, text="Place flags", variable=var_flag).grid(row=board.num_rows, column=board.num_cols)

# ADD BTN_SAVE
# ADD BTN_LOAD


m.title("Game")

m.mainloop()
