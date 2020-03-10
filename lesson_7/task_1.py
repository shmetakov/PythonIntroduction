from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.data = deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.data)

    def __add__(self, other):
        if len(self.data) != len(other.data) or \
                len(self.data[0]) != len(other.data[0]):
            return "Сложение матриц невозможно! Размерности не совпадают"

        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                sum_el = self.data[i][j] + other.data[i][j]
                row.append(sum_el)

            result.append(row)

        return Matrix(result)


matrix_list_1 = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

matrix_list_2 = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

matrix_1 = Matrix(matrix_list_1)
matrix_2 = Matrix(matrix_list_2)
print(matrix_1)
print()
print(matrix_1 + matrix_2)
