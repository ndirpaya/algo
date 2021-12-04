def rotate(self, matrix):
    self.transpose(matrix)
    self.reflect(matrix)

def transpose(self, matrix):
    n = len(matrix)
    for i in range (n):
        for j in range (i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

def reflect(self, matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

print(rotate(matrix))