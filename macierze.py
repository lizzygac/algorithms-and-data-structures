class Macierz:
    def __init__(self, data, par = 0):
        if isinstance(data, tuple):
            self.__matrix = [ [par for j in range(data[1])] for i in range(data[0]) ]
        else:
            self.__matrix = data

    def size(self):
        return (len(self.__matrix), len(self.__matrix[0]))

    def __add__(self, other):
        sizer = self.size()
        if sizer == other.size():
            return(Macierz([ [ self[i][j]+other[i][j] for j in range(sizer[1])] for i in range(sizer[0])]))
        else:
            raise Exception("Zły rozmiar macierzy!")

    def __mul__(self, other):
        sizerself = self.size()
        sizerother = other.size()

        if (sizerself[0] == sizerother[1]) and (sizerself[1] == sizerother[0]):
            return Macierz([[sum(self[i][k] * other[k][j] for k in range(other.size()[0])) for j in range(other.size()[1])] for i in range(self.size()[0]) ])
        else:
            raise Exception("Zły rozmiar macierzy!")

    def __getitem__(self, index):
        return self.__matrix[index]

    def __str__(self):
        text = ''
        for i in self.__matrix:
            text += '| '
            for j in i:
                text += str(j) + ' '
            text +='|\n'
        return text

def transpose(matrix):
    if isinstance(matrix, Macierz):
        sizer = matrix.size()
        return Macierz( [[ matrix[i][j] for i in range(sizer[0]) ] for j in range(sizer[1])])
    else:
            raise Exception("Złe dane wejściowe!")

def main():
    matrix = Macierz([[1, 0, 2],
                      [-1, 3, 1]])
    print(transpose(matrix))
    matrix2 = Macierz((2, 3), 1)
    matrix3 = matrix + matrix2
    print(matrix3)
    matrix4 = Macierz([[3, 1],
                      [2, 1], 
                      [1, 0]])
    matrix5 = matrix*matrix4
    print(matrix5)
    
main()