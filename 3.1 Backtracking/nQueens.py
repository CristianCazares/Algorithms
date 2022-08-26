from turtle import back


def showMatrix(m):
    for row in m:
        print(row)
    print("")

def isValid(inMat):
    queenCountRow=0
    queenCountColumn=0

    #Dimensions for the matrix
    ceiling=0
    floor=len(inMat)-1
    left=0
    right=floor

    for i in range(len(inMat)):
        queenCountRow=0
        queenCountColumn=0
        for j in range(len(inMat)):
            if inMat[i][j]!=0:
                queenCountRow+=1
                if queenCountRow>1:
                    return False
            
                #Explore bottom right diagonal
                currRow=i+1
                currColumn=j+1

                while currRow<=floor and currColumn<=right:
                    if inMat[currRow][currColumn]!=0:
                        #print("bottom right collision")
                        return False
                    currRow+=1
                    currColumn+=1
                
                #Explore bottom left diagonal

                currRow=i+1
                currColumn=j-1

                while currRow<=floor and currColumn>=left:
                    if inMat[currRow][currColumn]!=0:
                        #print("bottom left collision")
                        return False
                    currRow+=1
                    currColumn-=1
                
                #Explore top right diagonal

                currRow=i-1
                currColumn=j+1

                while currRow>=ceiling and currColumn<=right:
                    if inMat[currRow][currColumn]!=0:
                        #print("top right collision")
                        return False
                    currRow-=1
                    currColumn+=1
                
                #Explore top left diagonal

                currRow=i-1
                currColumn=j-1

                while currRow>=ceiling and currColumn>=left:
                    if inMat[currRow][currColumn]!=0:
                        #print("top left collision")
                        return False
                    currRow-=1
                    currColumn-=1


            if inMat[j][i]!=0:
                queenCountColumn+=1
                if queenCountColumn>1:
                    return False

    return True

def isSolution(m, nthQueen):
    if isValid(m) and nthQueen == len(m):
        return True
    return False

def backtracking(matrix, nthQueen, sol):
    for i in range(len(matrix)):
        m = [row[:] for row in matrix]
        m[nthQueen - 1][i] = nthQueen

        if not isValid(m):
            continue
        
        if isSolution(m, nthQueen):
            sol.append(m)
            return m

        backtracking(m, nthQueen + 1, sol)




def main():
    boardLength = int(input("Enter a board dimension: "))
    
    board = [[0 for _ in range(boardLength)] for _ in range(boardLength)]
    solution = []
    backtracking(board, 1, solution)


    print(f"Found {len(solution)} solutions for queens on a {boardLength} x {boardLength} board.")
    for sol in solution:
        showMatrix(sol)
    

main()