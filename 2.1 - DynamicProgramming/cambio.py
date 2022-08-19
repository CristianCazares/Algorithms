import os
os.system("cls||clear")
def showMatrix(m):
    for row in m:
        print(row)

cambio = 8
coins = [0, 2, 3, 7]
denomination = len(coins) - 1 

matrix = [[None for _ in range(cambio + 1)] for _ in range(len(coins))]

def change(i, remain):
    if matrix[i][remain] != None:
        return matrix[i][remain]

    if remain == 0:
        matrix[i][remain] = 0
        return matrix[i][remain]
    elif i == 0 and remain != 0:
        matrix[i][remain] = float('inf')
        return matrix[i][remain]

    if coins[i] > remain:
        matrix[i][remain] = change(i - 1, remain)
        return matrix[i][remain]
    else:
        matrix[i][remain] = min(
            change(i - 1, remain),
            change(i, remain - coins[i]) + 1
            )
        return matrix[i][remain]
    


def changeRec(i, remain):
    if remain == 0:
        return 0
    elif i == 0 and remain != 0:
        return float('inf')
    

    if coins[i] > remain:
        return changeRec(i - 1, remain)
    else:
        return min(
            changeRec(i - 1, remain),
            changeRec(i, remain - coins[i]) + 1
            )

def getCoins():
    coinDic = {}
    for coin in coins:
        coinDic[coin] = 0
    
    print(coinDic)
    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    while j > 0:
        if i > 1 and matrix[i][j] == matrix[i - 1][j]:
            i -= 1
        else:
            coinDic[coins[i]] += 1
            j-=coins[i]
            

    print(coinDic)

nCoins = change(denomination, cambio)
showMatrix(matrix)
print(nCoins)

getCoins()