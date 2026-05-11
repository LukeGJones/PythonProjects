def printMatrix(matrix):
    for row in matrix:
        print(row)

def createSubMatrix(i, j, matrix):
    subMatrix = []
    for iIndex, row in enumerate(matrix):
        if iIndex != i:
            newRow = []
            for jIndex, item in enumerate(row):
                if(jIndex != j):
                    newRow.append(item)
            subMatrix.append(newRow)
    return subMatrix

def determinantCalc(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if(len(matrix) == 2):  
        determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return determinant
    
    determinant = 0
    for j in range(len(matrix)):
        subMatrix = createSubMatrix(0, j, matrix)
        sign = (-1) ** j
        determinant += sign * matrix[0][j] * determinantCalc(subMatrix)
    return determinant

def cofactorMatrixCalc(matrix, size):
    cofactorMatrix = []
    for i in range(size):
        newRow = []
        for j in range(size):
            newRow.append(0)
        cofactorMatrix.append(newRow)

    for i in range(size):
        for j in range(size):
            tempMatrix = createSubMatrix(i, j, matrix)
            cofactorMatrix[i][j] = (-1)**(i+j) * determinantCalc(tempMatrix)

    return cofactorMatrix

def transposeMatrixCalc(matrix, size):
    transposedMatrix = []
    for i in range(size):
        newRow = []
        for j in range(size):
            newRow.append(0)
        transposedMatrix.append(newRow)

    for i in range(size):
        for j in range(size):
            transposedMatrix[j][i] = matrix[i][j]
            
    return transposedMatrix


matrix = []
row = 0
column = 0
size = int(input("Enter size of one side of square matrix: "))
for i in range(size):
    newRow = []
    for j in range(size):
        inp = int(input("Enter a number to go into row " + str(row + 1) + " column " + str(column + 1) + ":"))
        column += 1
        newRow.append(inp)
    row += 1
    column = 0
    matrix.append(newRow)

printMatrix(matrix)
print()
printMatrix(transposeMatrixCalc(matrix, size))

