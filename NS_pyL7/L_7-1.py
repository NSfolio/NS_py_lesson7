from itertools import zip_longest


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                       for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])


m = [[1, 5, 7], [8, 6, 4], [3, 9, 2]]
n = [[6, 3, 8], [4, 2, 5], [9, 7, 1]]


matr_1 = Matrix(m)
matr_2 = Matrix(n)

print(matr_1)
print('*************')
print(matr_2)
print('*************')
print(matr_1 + matr_2)
