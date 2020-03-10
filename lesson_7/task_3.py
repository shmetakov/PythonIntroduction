class Cell:
    def __init__(self, size):
        self.__size = size

    def __add__(self, other):
        return Cell(self.__size + other.__size)

    def __sub__(self, other):
        if self.__size - other.__size < 0:
            print("Операция невозможна!")
            return Cell(0)
        else:
            return Cell(self.__size - other.__size)

    def __mul__(self, other):
        return Cell(self.__size * other.__size)

    def __truediv__(self, other):
        return Cell(self.__size // other.__size)

    def make_order(self, size):
        return ''.join(['*' if i % size != 0 else '*\n' for i in range(1, self.__size + 1)])


cell_1 = Cell(6)
cell_2 = Cell(2)

print("Сложение")
res = cell_1 + cell_2
print(res.make_order(5))

print("Вычитание")
res = cell_1 - cell_2
print(res.make_order(6))

print("Умножение")
res = cell_1 * cell_2
print(res.make_order(2))

print("Деление")
res = cell_1 / cell_2
print(res.make_order(4))