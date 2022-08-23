def showMatrix(m):
    for row in m:
        print(row)
    print("")

class Tree:
    def __init__(self, data):
        self.data = data
        self.childs = []

def backtracking(matrix, queenPos, nQueen, queensAmount):
    showMatrix(matrix)
    m = matrix
    m[queenPos[0]][queenPos[1]] = 1
    matrix[queenPos[0]][queenPos[1]] = 0


def main():
    boardLength = 4
    board = [[0 for _ in range(boardLength)] for _ in range(boardLength)]
    
    backtracking(board, [0,1], 1, 4)

    #for i in range(boardLength):
        #showMatrix(board)

main()