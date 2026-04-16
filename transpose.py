def transpose(matrix):
    row=len(matrix)
    col=len(matrix[0])
    result=[[0 for i in range(row)] for j in range(col)]
    for i in range(row):
        for j in range(col):
            result[j][i]=matrix[i][j]
    return result

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))