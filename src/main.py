
board =[["-","-","-","-","-","-","-"],
["-","-","-","-","-","-","-"],
["-","-","-","-","-","-","-"],
["-","-","-","-","-","-","-"],
["-","-","-","-","-","-","-"],
["-","-","-","-","-","-","-"]]


def printBoard(board):
    for line in board:
        print(line)

def getInput():
    row = int(input("Enter a row to place token: (1-7)"))
    if row > 0 and row < 8:
        return row
    else:
        print("Input is not valid")
        row = int(input("Enter a row to place token: (1-7)"))
    return row

def updateBoard(board, input):
    row = -1
    if board[row][input-1] == "-":
        board[row][input-1] = "R"
    else:
        row = -2
        board[row][input-1] = "R"
    



def main():
    printBoard(board)
    row = getInput()
    updateBoard(board, row)
    printBoard(board)

if __name__ == "__main__":
    main()
    quit