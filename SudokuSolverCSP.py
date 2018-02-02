import math

example1 = [[-1,-1,-1,2,6,-1,7,-1,1],
           [6,8,-1,-1,7,-1,-1,9,-1],
           [1,9,-1,-1,-1,4,5,-1,-1],
           [8,2,-1,1,-1,-1,-1,4,-1],
           [-1,-1,4,6,-1,2,9,-1,-1],
           [-1,5,-1,-1,-1,3,-1,2,8],
           [-1,-1,9,3,-1,-1,-1,7,4],
           [-1,4,-1,-1,5,-1,-1,3,6],
           [7,-1,3,-1,1,8,-1,-1,-1]]

blank = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1],
           [-1,-1,-1,-1,-1,-1,-1,-1,-1]]


def printSudoku(sudoku):
    nRow = 0
    for row in sudoku:

        if (nRow == 3):
            nRow = 0

        if (nRow == 0):
            print("===================")
        else:
            print("-------------------")

        nRow += 1

        nCol = 0
        for item in row:

            if (nCol == 3):
                nCol = 0

            if (nCol == 0):
                print('‖', end="")

            else:
                print('|', end="")

            nCol += 1

            if item == -1:
                print(" ", end="")

            else:
                print(item, end="")

        print("|")




def getAvailableList(sudoku):

    #[row][col][available node]
    available_list = []
    for i in range(9):
        available_list.append([])
        for j in range(9):

            if(sudoku[i][j] == -1):

                available = set([k for k in range(1, 10)])
                notAvailable = set()

                rowValues = set(sudoku[i])

                colValues = set([m[j] for m in sudoku])

                boxValues = set()
                boxRow = 3 * math.floor(i/3)
                boxCol = 3 * math.floor(j/3)
                for u in range(boxRow, boxRow + 3):
                    for v in range(boxCol, boxCol + 3):
                        boxValues.add(sudoku[u][v])

                notAvailable = colValues.union(rowValues.union(boxValues))
                notAvailable.remove(-1)

                available_list[i].append(available.difference(notAvailable))

            else:
                available_list[i].append(set())

    print(available_list)




if __name__ == "__main__":
    getAvailableList(example1)

