import random
import math
import tkinter

# board set up
boardSize = random.randint(2, 20)
board = [[0 for row in range(boardSize)] for column in range(boardSize)]
tiles = []


def placeBomb(x, y):
    board[y][x] = "X"
    if (0 <= x <= boardSize - 2) and (0 <= y <= boardSize - 1):
        if board[y][x + 1] != 'X':
            board[y][x + 1] += 1  # center right
    if (1 <= x <= boardSize - 1) and (0 <= y <= boardSize - 1):
        if board[y][x - 1] != 'X':
            board[y][x - 1] += 1  # center left
    if (1 <= x <= boardSize - 1) and (1 <= y <= boardSize - 1):
        if board[y - 1][x - 1] != 'X':
            board[y - 1][x - 1] += 1  # top left
    if (0 <= x <= boardSize - 2) and (1 <= y <= boardSize - 1):
        if board[y - 1][x + 1] != 'X':
            board[y - 1][x + 1] += 1  # top right
    if (0 <= x <= boardSize - 1) and (1 <= y <= boardSize - 1):
        if board[y - 1][x] != 'X':
            board[y - 1][x] += 1  # top center
    if (0 <= x <= boardSize - 2) and (0 <= y <= boardSize - 2):
        if board[y + 1][x + 1] != 'X':
            board[y + 1][x + 1] += 1  # bottom right
    if (1 <= x <= boardSize - 1) and (0 <= y <= boardSize - 2):
        if board[y + 1][x - 1] != 'X':
            board[y + 1][x - 1] += 1  # bottom left
    if (0 <= x <= boardSize - 1) and (0 <= y <= boardSize - 2):
        if board[y + 1][x] != 'X':
            board[y + 1][x] += 1  # bottom center


def game():
    gameBoard = tkinter.Tk()
    gameBoard.title("Minesweeper AQ")
    frame = tkinter.Frame(master=gameBoard)

    def revealNeighbours(row, column):
        neighbours = [
            {"x": row - 1, "y": column - 1},  # top-left
            {"x": row - 1, "y": column},  # top-middle
            {"x": row - 1, "y": column + 1},  # top-right
            {"x": row, "y": column - 1},  # middle-left
            {"x": row, "y": column + 1},  # middle-right
            {"x": row + 1, "y": column - 1},  # bottom-left
            {"x": row + 1, "y": column},  # bottom-middle
            {"x": row + 1, "y": column + 1},  # bottom-right
        ]
        for n in neighbours:
            try:
                if board[n["x"]][n["y"]] != 'X':
                    tiles[n["x"]][n["y"]]['text'] = board[n["x"]][n["y"]]
                    tiles[n["x"]][n["y"]]['state'] = "disabled"
            except:
                pass

    def checkWin():
        blankTiles = []
        for r in range(boardSize):
            for c in range(boardSize):
                if tiles[r][c]['text'] == "":
                    blankTiles.append({"r": r, "c": c})

        if len(blankTiles) == bombs:
            for cell in blankTiles:
                tiles[cell["r"]][cell["c"]]['text'] = "Win"
                tiles[cell["r"]][cell["c"]]['bg'] = "Green"
                tiles[cell["r"]][cell["c"]]['state'] = "disabled"

    def gameLost():
        for r in range(boardSize):
            for c in range(boardSize):
                if board[r][c] == "X":
                    tiles[r][c]['text'] = "Lose"
                    tiles[r][c]['bg'] = "Red"
                tiles[r][c]['state'] = "disabled"

    def reveal(row, column):
        if board[row][column] == "X":
            gameLost()
        else:
            tiles[row][column]['text'] = board[row][column]
            tiles[row][column]['state'] = "disabled"
            revealNeighbours(row, column)
            checkWin()

    for row in range(boardSize):
        tiles.append([])
        for column in range(boardSize):
            btnValue = f"{board[row][column]}"
            tiles[row].append(
                tkinter.Button(master=frame, width=3, command=lambda row=row, column=column: reveal(row, column)))
            tiles[row][column].grid(row=row, column=column)
    frame.pack()
    gameBoard.mainloop()


if __name__ == '__main__':
    # randomly place bombs
    bombs = math.ceil(0.30 * (boardSize ^ 2))
    for b in range(bombs):
        placeBomb(random.randint(0, boardSize - 1), random.randint(0, boardSize - 1))

    # game logic
    game()
