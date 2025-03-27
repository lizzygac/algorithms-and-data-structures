class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ':'+ str(self.value)

class Mixedtab:

    def __init__(self, size, c1 = 1, c2 = 0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    
    def collide(self, index, i):
        nindex =  (index + self.c1 * i + self.c2 * i **2) % self.size
        return nindex

    def mix(self, key):
        if isinstance(key, str):
            x = 0
            for i in key:
                x += ord(i)
        elif isinstance(key, int):
            x = key
        else:
            raise Exception('Zły typ danych')
        return x % self.size
    
    def search(self, key):
        index = self.mix(key)
        if self.tab[index] is not None and self.tab[index].key == key:
            return self.tab[index].value
        else:
            for i in range(1, self.size + 1):
                nindex = self.collide(index, i)
                if self.tab[nindex] is not None:
                    if  self.tab[nindex].key == key:
                        return self.tab[nindex].value
        return None

    def insert(self, key, value):
        index = self.mix(key)
        if self.tab[index] is None:
            self.tab[index] = Element(key, value)
        else:
            if self.tab[index].key == key:
                self.tab[index].value = value
            else:
                sukces = False
                for i in range(1, self.size + 1):
                    nindex = self.collide(index, i)
                    if self.tab[nindex] is None:
                        sukces = True
                        break
                if sukces:
                    self.tab[nindex] = Element(key, value)
                else:
                    print('Brak miejsca')


    def remove(self, key):
        index = self.mix(key)
        if self.tab[index] is not None and self.tab[index].key == key:
            self.tab[index].key = None
            self.tab[index].value = None
            self.tab[index] = None
        else:
            for i in range(1, self.size +1):
                nindex = self.collide(index, i)
                if self.tab[nindex] is not None:
                    if  self.tab[nindex].key == key:
                        self.tab[nindex].key = None
                        self.tab[nindex].value = None
                        self.tab[nindex] = None
                    
                if i == self.size - 1:
                    print('Brak danej')

    def __str__(self):
        st = "{"
        for i in range(self.size):
            st += self.tab[i].__str__()
            if i != self.size - 1:
                st += ', '
        st += "}"
        return st

def test(c1 = 1, c2 = 0):
    mix = Mixedtab(13, c1, c2)
    mix.insert(1,'A')
    mix.insert(2,'B')
    mix.insert(3,'C')
    mix.insert(4,'D')
    mix.insert(5,'E')
    mix.insert(18,'F')
    mix.insert(31,'G')
    mix.insert(8,'H')
    mix.insert(9,'I')
    mix.insert(10,'J')
    mix.insert(11,'K')
    mix.insert(12,'L')
    mix.insert(13,'M')
    mix.insert(14,'N')
    mix.insert(15,'O')
    print(mix)
    print(mix.search(5))
    print(mix.search(14))
    mix.insert(5, 'Z')
    print(mix.search(5))
    mix.remove(5)
    print(mix)
    print(mix.search(31))
    mix.insert('test', 'W')
    print(mix)

def test2(c1 = 1, c2 = 0):
    mix = Mixedtab(13, c1, c2)
    mix.insert(13,'A')
    mix.insert(26,'B')
    mix.insert(39,'C')
    mix.insert(52,'D')
    mix.insert(65,'E')
    mix.insert(78,'F')
    mix.insert(91,'G')
    mix.insert(104,'H')
    mix.insert(117,'I')
    mix.insert(130,'J')
    mix.insert(143,'K')
    mix.insert(156,'L')
    mix.insert(169,'M')
    mix.insert(182,'N')
    mix.insert(195,'O')
    print(mix)
    

def main():
    test(1, 0)
    test2(1, 0)
    test2(0, 1)
    test(0, 1)
    

main()
