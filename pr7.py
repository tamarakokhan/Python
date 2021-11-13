# задача 2
from abc import ABC, abstractmethod

print("Задача 1")


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join([f'{i}\t' for i in row]) for row in self.matrix])

    def __add__(self, other):
        total_matrix = []
        for i in range(len(self.matrix)):
            total_matrix_1 = []
            for j in range(len(other.matrix)):
                total_matrix_1.append(self.matrix[i][j] + other.matrix[i][j])
            total_matrix.append(total_matrix_1)

        # total_matrix = [[x + y for x, y in zip(w, v)] for w, v in zip(self.matrix, other.matrix)]

        return Matrix(total_matrix)


matrix_1 = Matrix([[2, 1222, 2], [2, 1222, 2], [2, 1222, 2]])
matrix_2 = Matrix([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
print(matrix_1 + matrix_2)

print("Задача 2")


class Clothes(ABC):
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def tissue_consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def tissue_consumption(self):
        return 2 * self.h + 0.3


coat_1 = Coat(6.5)
suit_1 = Suit(1.35)
print(f"Общий расход ткани на пальто и костюм: {coat_1.tissue_consumption + suit_1.tissue_consumption}")

print("Задача 3")


class Cell:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f"{self.n}"

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if (self.n - other.n) >= 0:
            return Cell(self.n - other.n)
        else:
            return "Действие невозможно, результат < 0."

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(self.n // other.n)

    def make_order(self, n_in_row):
        return '\n'.join("*" * n_in_row for _ in range(self.n // n_in_row)) + "\n" + "*" * (self.n % n_in_row)


cell_1 = Cell(10)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(2))
