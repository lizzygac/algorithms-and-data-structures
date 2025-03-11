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
    
    def __setitem__(self, index, item):
        self.__matrix[index] = item

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
    
def determinant2x2(matrix):
    if isinstance(matrix, Macierz):
        if matrix.size() == (2, 2):
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        else:
            raise Exception("Zły rozmiar macierzy!")
    else:
        raise Exception("Złe dane wejściowe!")

def chio(matrix):
    if isinstance(matrix, Macierz):
        sizer = matrix.size()
        if sizer == (2, 2):
            return determinant2x2(matrix)
        elif sizer[0] != sizer[1]:
            raise Exception("Zły rozmiar macierzy!")            
        else:
            sign = 1
            if matrix[0][0] == 0:
                for i in range(matrix.size()[0]):
                    if matrix[i][0] != 0:
                        matrix[0], matrix[i] = matrix[i], matrix[0]
                        sign = -1
                        break
            return sign/((matrix[0][0]**(matrix.size()[0]-2)))*chio(Macierz([ [ determinant2x2(Macierz([[matrix[0][0], matrix[0][j+1]], [matrix[i+1][0], matrix[i+1][j+1]]])) for j in range(sizer[0]-1)] for i in range((sizer[0]-1))]))
    else:
        raise Exception("Złe dane wejściowe!")
    
def main():
    matrix = Macierz([
        [5 , 1 , 1 , 2 , 3],
        [4 , 2 , 1 , 7 , 3],
        [2 , 1 , 2 , 4 , 7],
        [9 , 1 , 0 , 7 , 0],
        [1 , 4 , 7 , 2 , 2]
        ])
    print(chio(matrix))

    matrix2 = Macierz( [
        [0 , 1 , 1 , 2 , 3],
        [4 , 2 , 1 , 7 , 3],
        [2 , 1 , 2 , 4 , 7],
        [9 , 1 , 0 , 7 , 0],
        [1 , 4 , 7 , 2 , 2]
        ])

    print(chio(matrix2))

main()