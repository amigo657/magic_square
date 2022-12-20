class Create():

    def __init__(self, n):
        self.n = n

    def generateSquare(self):

        #создание матрицы
        self.magicSquare = [[0 for x in range(self.n)] for y in range(self.n)]

        self.i = self.n // 2      #строки
        self.j = self.n - 1       #столбцы

        #заполнение квадрата
        self.num = 1
        while self.num <= (self.n * self.n):
            #третье условие заполнения
            if self.i == -1 and self.j == self.n:
                self.i = 0
                self.j = self.n - 2
            else:
                #если j = n
                if self.j == self.n:
                    self.j = 0
                
                #если i = -1
                if self.i < 0:
                    self.i = self.n - 1

            # проверка наличия элемента в вычисленной позиции
            if self.magicSquare[int(self.i)][int(self.j)]:
                self.j = self.j - 2
                self.i = self.i + 1
                continue
            else:
                self.magicSquare[int(self.i)][int(self.j)] = self.num
                self.num = self.num + 1

            self.j = self.j + 1
            self.i = self.i - 1

        # print("Magic Square for n =", self.n)
        # print("Sum of each row or column", self.n * (self.n * self.n + 1) // 2, "\n")

        # # вывод
        # for i in self.magicSquare:
        #     for j in i:
        #         print('%2d ' % j, end = "")
        #     print()
        return self.magicSquare