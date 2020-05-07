""" Programmed by John D Ryan"""

import random


class MineBoard:
    def __init__(self, rows, col, difficulty, attempts):
        self.num_rows = rows
        self.num_cols = col
        self.num_tiles = rows * col
        self.difficulty = difficulty
        self.num_mines = int(self.setMineNum())
        self.game_state = True
        self.attempts = attempts
        self.tile_content = [[]]
        self.tile_state = [[]]

        self.initializeBoard()
        self.placeMines()
        """print("")
        for x in range(self.num_rows):
            print(self.tile_content[x])
        print(self.tile_state)"""

    """///////////////////
    ////// Functions /////
    ///////////////////"""

    # Sets lists representing rows and columns to default states
    def initializeBoard(self):
        self.tile_content = [[0]*self.num_cols for _ in range(self.num_rows)]
        self.tile_state = [[0]*self.num_cols for _ in range(self.num_rows)]

    # Places mines in random locations on the minesweeper board
    def placeMines(self):
        mines_placed = 0
        print(self.num_mines)
        while self.num_mines - mines_placed > 0:
            place_row = random.randint(0, self.num_rows - 1)
            place_col = random.randint(0, self.num_cols - 1)
            if not self.hasMine(place_row, place_col):
                self.addMine(place_row, place_col)
                mines_placed = mines_placed + 1

    # Returns true if the tile is in a valid location, false otherwise:
    def isValidTile(self, r, c, flag = False):
        try:
            self.tile_content[r][c] = self.tile_content[r][c] # Will throw an IndexError if row and column are invalid
            if c < 0 or r < 0 or c == self.num_cols or r == self.num_rows:
                return False
            return True
        except(IndexError):
            return False

    # Returns true if the tile contains a mine, false otherwise
    def hasMine(self, r, c):
        return self.getContent(r, c) == 9

    # Places a mine at specified row and column
    def addMine(self, r, c):
        self.tile_content[r][c] = 9
        self.incrementNearby(r, c)

    # Adds flag to specified row and column
    def addFlag(self, r, c):
        if self.canAddFlag(r, c):
            self.tile_state[r][c] = 2

    # Removes flag from specified row and column
    def removeFlag(self, r, c):
        if self.canRemoveFlag(r, c):
            self.tile_state[r][c] = 0

    # Increments number count of nearby tiles that don't contain mines
    def incrementNearby(self, r, c):
        row = r - 1
        while row < (r + 2):
            col = c - 1
            while col < (c + 2):
                if self.isValidTile(row, col):
                    if not self.hasMine(row, col):
                        # print(str(self.tile_content[row]) + " " + str(row) + " " + str(col))  # Debugging
                        self.tile_content[row][col] += 1
                        # print(str(self.tile_content[row]) + " " + str(row) + " " + str(col))  # Debugging
                        # This isn't working correctly, it's incrementing values on the other side of the board
                    # print("")  # Debugging
                col += 1
            row += 1

    def hasFlag(self, r, c):
        return self.getState(r, c) == 2

    # Returns true if flag can be added to given coordinates
    def canAddFlag(self, r, c):
        return self.isCovered(r, c) and not self.hasFlag(r, c)

    # Returns true if the flag can be removed
    def canRemoveFlag(self, r, c):
        return self.tile_state[r][c] == 2

    # Returns true if the tile at specified row and column is covered
    # 2 represents a tile with a flag and 0 represents a covered tile, both will be considered covered for this function
    def isCovered(self, r, c):
        return not self.getState(r, c) == 1

    # Sets number of mines based on difficulty of game
    def setMineNum(self):
        if self.difficulty == 1:  # Easy
            return self.num_tiles / 10
        elif self.difficulty == 2:  # Medium
            return self.num_tiles / 8
        else:  # Hard
            return self.num_tiles / 6

    # Clears lists making up board and sets attempts_remaining to default
    def clearBoard(self):
        pass

    # Resets board back to original state with mines placed identically
    def resetGame(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.tile_state[r][c] = 0

    # Subtracts one attempt from attempts remaining
    def subAttempt(self):
        self.attempts = self.attempts - 1

    # Returns content in tile at r, c
    def getContent(self, r, c):
        return self.tile_content[r][c]

    # Returns state of tile at r, c
    def getState(self, r, c):
        return self.tile_state[r][c]

    # Returns number of mines placed on board
    def getMinesPlaced(self):
        num_placed = 0
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if self.hasMine(r, c):
                    num_placed = num_placed + 1
        return num_placed

    # Returns number representing how many mines have been uncovered
    def getMinesUncovered(self):
        uncovered_mines = 0
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if self.hasMine(r, c) and not self.isCovered(r, c):
                    uncovered_mines = uncovered_mines + 1
        return uncovered_mines

    # Returns number of uncovered squares
    def getSquaresUncovered(self):
        uncovered_squares = 0
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if not self.isCovered(r, c) and not self.hasFlag(r, c):
                    uncovered_squares = uncovered_squares + 1
        return uncovered_squares

    # Returns the number of flags that have been placed
    def getNumFlags(self):
        placed_flags = 0
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if self.hasFlag(r, c):
                    placed_flags = placed_flags + 1
        return placed_flags

    # Returns the number of attempts remaining
    def getAttemptsRemaining(self):
        return self.attempts

    # Returns what text should be shown for specified tile, given its current state and content
    def getCurrentShownText(self, r, c):
        current_text = " "
        current_state = self.getState(r, c)
        current_content = self.getContent(r, c)
        if current_state == 0:
            current_text = " "  # Covered tile
        elif current_state == 1:
            if current_content == 9:
                current_text = "*"  # Uncovered Mine
            elif current_content == 0:
                current_text = " "  # Uncovered blank space
            else:
                current_text = str(current_content)  # string representation of number at tile
        elif current_state == 2:
            current_text = "#"  # placed flag

        return current_text

    # Returns true if any tiles nearby are covered, false otherwise
    def areNearbyCovered(self, r, c):
        pass

    # Returns true if any tiles naerby are empty
    def areNearbyEmptyAndUncovered(self, r, c):
        pass

    # Returns true if tile at row and column contains a number
    def hasNumber(self, r, c):
        return 0 < self.tile_content[r][c] < 9

    # Returns true if tile at row and colun is empty, false otherwise
    def isEmpty(self, r, c):
        return self.tile_content[r][c] == 0

    # Uncover only the tile located at row and column
    def uncoverExact(self, r, c):
        self.tile_state[r][c] = 1

    # Processes result of user selecting tile at r, c
    def processMove(self, r, c):
        if not self.isCovered(r, c):
            print("The tile at location (" + str(r+1) + ", " + str(c+1) + ") is already uncovered.")
        elif self.isEmpty(r, c): # Empty square
            self.processBlank(r, c)
        elif self.hasMine(r, c):
            self.subAttempt()
        self.uncoverExact(r, c)

    # Processes what to do if a blank tile is uncovered
    def processBlank(self, r, c):
        to_uncover = [[0]*self.num_cols for _ in range(self.num_rows)]  # Stores locations that need to be uncovered
        past_index = [0] * self.num_tiles * 2  # Stores what row/col tiles have been parsed through
        more_blank = True  # Remains true while there's still more blank tiles to uncover
        can_add_blank = True  # Remains true while there are blank tiles adjacent to current coordinates
        row = r
        col = c
        index = 0  # Keeps track of current index being used by past_index list
        begin_index = 0  # If this equals index after the 8 below if statements, no adjacent empty spots can be found
        num_adj = 0  # Keeps track of how many adjacent blank tiles have been added to to_uncover

        while more_blank:
            while can_add_blank:
                begin_index = index

                if self.isValidTile(row - 1, col):
                    if self.isEmpty(row-1, col) and to_uncover[row-1][col] != 1:
                        to_uncover[row-1][col] = 1
                        past_index[index] = row
                        index += 1
                        past_index[index] = col
                        index += 1
                        row -= 1
                if self.isValidTile(row, col-1):
                    if self.isEmpty(row, col-1) and to_uncover[row][col-1] != 1:
                        to_uncover[row][col-1] = 1
                        past_index[index] = row
                        index += 1
                        past_index[index] = col
                        index += 1
                        col -= 1
                if self.isValidTile(row+1, col):
                    if self.isEmpty(row+1, col) and to_uncover[row+1][col] != 1:
                        to_uncover[row+1][col] = 1
                        past_index[index] = row
                        index += 1
                        past_index[index] = col
                        index += 1
                        row += 1
                if self.isValidTile(row, col + 1):
                    if self.isEmpty(row, col + 1) and to_uncover[row][col + 1] != 1:
                        to_uncover[row][col + 1] = 1
                        past_index[index] = row
                        index += 1
                        past_index[index] = col
                        index += 1
                        col += 1

                # Ensures no index is past_index will contain any empty adjacent tiles
                if begin_index == index and can_add_blank:
                    if index != 0:
                        index -= 2
                        row = past_index[index]
                        col = past_index[index + 1]
                    else:
                        can_add_blank = False
                # Increments num_adj
                elif can_add_blank:
                    num_adj += 1
            row = r
            col = c
            if num_adj == 0:
                more_blank = False
            num_adj = 0

        # Uncovering empty tiles
        for x in range(self.num_rows):
            for y in range(self.num_cols):
                if to_uncover[x][y] == 1 and self.isEmpty(x, y):
                    self.uncoverNearby(x, y)
                elif to_uncover[x][y] == 1:
                    self.uncoverExact(x, y)

        # Logic for uncovering tiles with numbers that are adjacent to empty tiles that have been uncovered
        for x in range(self.num_rows):
            for y in range(self.num_cols):
                if self.areNearbyEmptyAndUncovered(x, y) and self.hasNumber(x, y):
                    to_uncover[x][y] = 1

        # Uncovering empty tiles
        for x in range(self.num_rows):
            for y in range(self.num_cols):
                if to_uncover[x][y] == 1 and self.isEmpty(x, y):
                    self.uncoverNearby(x, y)

        # print(past_index)  # Debug

    # Uncovers every mine (in event player wins/loses)
    def uncoverAllMines(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if self.tile_content[r][c] == 9:
                    self.tile_state[r][c] = 1

    # Uncovers every nearby square. Apply on an empty square
    def uncoverNearby(self, r, c):
        row = r - 1
        while row < (r + 2):
            col = c - 1
            while col < (c + 2):
                if self.isValidTile(row, col):
                    if (self.isCovered(row, col) or self.hasFlag(row, col) and (not col == c or not row == r)):
                        # print(str(self.tile_content[row]) + " " + str(row) + " " + str(col))  # Debugging
                        self.tile_state[row][col] = 1
                        # print(str(self.tile_content[row]) + " " + str(row) + " " + str(col))  # Debugging
                        # This isn't working correctly, it's incrementing values on the other side of the board
                    # print("")  # Debugging
                col += 1
            row += 1

    # Uncovers every tile on the board
    def uncoverBoard(self):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.tile_state[r][c] = 1

    def boardInfo(self):
        return "Attempts remaining: " + str(self.attempts) + " | Mines remaining: " + str(
            self.num_mines - self.getNumFlags())

    # Outputs a representation of the board to the console, pretty much used only while debugging as the tkinter
    # implemntation works much more efficiently and comprehensively for testing.
    def showBoard(self):
        current_state = 0
        current_out = " "
        current_content = 0
        self.boardInfo();
        print("  ", end="")
        for i in range(self.num_cols):
            print(str(i+1), end=" ")
        print("")
        for r in range(self.num_rows):
            print(str(r+1) + "|", end="")
            for c in range(self.num_cols):
                current_state = self.tile_state[r][c]
                current_content = self.tile_content[r][c]
                if current_state == 0:
                    current_out = " "  # Covered space
                elif current_state == 1:
                    if current_content == 9:
                        current_out = "*"  # Uncovered mine
                    elif current_content == 0:
                        current_out = "0"  # Uncovered blank space
                    else:
                        current_out = str(current_content)
                elif current_state == 2:
                    current_out = "#"  # Placed flag
                print(current_out, end="|")
            print("")

    # Saves game to game.txt
    def saveGame(self):
        file = open("game.txt", "w")
        file.write(str(self.num_rows) + "x" + str(self.num_cols) + "\n")

        for r in range(self.num_rows):
            for c in range(self.num_cols):
                file.write(str(self.tile_content[r][c]))  # Writing the content to the file
            file.write("\n")
        file.write("\n")

        for r in range(self.num_rows):
            for c in range(self.num_cols):
                file.write(str(self.tile_state[r][c]))  # Writing the state to the file
            file.write("\n")

        file.close()

    # Loads stored save game from game.txt
    def loadGame(self):
        file = open("game.txt", "r")
        current = str(self.num_rows) + "x" + str(self.num_cols) + "\n"

        if current != file.readline():
            return False
        else:
            for r in range(self.num_rows):
                current_tile_content = file.readline(r+1)
                current_tile_state = file.readline(r+2+self.num_rows)
                for c in range(self.num_cols - 1):
                    self.tile_content[r][c] = int(str(current_tile_content[c:c+1]))
                    self.tile_state[r][c] = int(str(current_tile_state[c:c+1]))
        file.close()


# Driver
"""board = MineBoard(5, 5, 3, 1)
board.uncoverAllMines()
board.uncoverBoard()
board.showBoard()
while board.attempts > 0:
    board.showBoard()
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    board.processMove(row, col)
"""
"""while board.attempts > 0:
    for x in range(board.num_rows):
        print(board.tile_content[x])
    print("")
    for x in range(board.num_rows):
        print(board.tile_state[x])
    print("What to uncover")
    board.uncoverAllMines()
    for x in range(board.num_rows):
        print(board.tile_state[x])
    board.attempts = 0"""