Number = 6

class Element:
    def __init__(self, next = None):
        self.tab = [None for i in range(Number)]
        self.numelem = 0
        self.next = next

    def add(self, data, index):
        elem = data
        if self.numelem == 0:
            self.tab[0] = data
            self.numelem = self.numelem + 1
        else:
            for i in range(index, self.numelem + 1):
                next = self.tab[i]
                self.tab[i] = elem
                elem = next
            self.numelem = self.numelem + 1

    def remove(self, index):
        if self.numelem == 1:
            x = self.tab[0]
            self.tab[0] = None
            self.numelem = self.numelem - 1
            return x
        else:
            x = self.tab[index]
            elem = None
            for i in range(index, self.numelem-1):
                self.tab[i] = self.tab[i+1]
            self.tab[self.numelem-1] = None
            self.numelem = self.numelem - 1
            return x


class Unrolledlist:
    def __init__(self):
        self.head = None

    def size(self):
        if self.head is None:
            return 0
        else:
            size = 0
            where = self.head
            while where is not None:
                size += where.numelem
                where = where.next
            return size

    def get(self, index):
        if index >= self.size():
            raise Exception('Index out of range!')
        else:
            where = self.head
            ind = index
            if ind > where.numelem:
                while where.next is not None:
                    ind -= where.numelem
                    where = where.next
            return where.tab[ind]

    def insert(self, data, index):
        if self.head is None:
            self.head = Element()
            self.head.add(data, 0)
        else:
            if index >= self.size():
                where = self.head
                while where.next is not None:
                    where = where.next
                nind = where.numelem
            else:
                where = self.head
                searching = True
                numelem = 0
                while searching:
                    if index < numelem + where.numelem:
                        searching = False
                        nind = index - numelem
                    else:
                        numelem += where.numelem
                        where = where.next
                        
            if where.numelem == Number:
                nelem = Element()
                for i in range(Number//2, Number):
                    nelem.add(where.remove(Number//2), i-(Number//2))
                if nind >= Number//2:
                    nind -= Number//2
                    nelem.add(data, nind)
                else:
                    where.add(data, nind)
                nextog = where.next
                where.next = nelem
                where.next.next = nextog
            else:
                where.add(data, nind)
            
    def delete(self, index):
        if self.head is None:
            raise Exception('There is nothing there')
        else:
            if index >= self.size():
                where = self.head
                while where.next is not None:
                    where = where.next
                nind = where.numelem
            else:
                where = self.head
                searching = True
                numelem = 0
                while searching:
                    if index < numelem + where.numelem:
                        searching = False
                        nind = index - numelem
                    else:
                        where = where.next
                        numelem += where.numelem

            where.remove(nind)

            if where.numelem < Number//2:
                nextelem = where.next
                nextnextog = nextelem.next
                while where.numelem < Number//2:
                    where.add(nextelem.remove(0), where.numelem)
                if nextelem.numelem < Number//2:
                    for i in range(nextelem.numelem):
                        where.add(nextelem.remove(0), where.numelem)
                where.next = nextnextog

    def __str__(self):
        if self.head is None:
            return 'lista pusta'
        else:
            io = '['
            where = self.head
            size = self.size()
            j = 0
            while where is not None:
                for i in range(where.numelem):
                    io += str(where.tab[i])
                    j += 1
                    if j != size:
                        io += ', '
                where = where.next
            io += ']'
            return io

def main():
    l = Unrolledlist()
    for i in range(1,10):
        l.insert(i, i)
    print(l.get(4))
    l.insert(10, 1)
    l.insert(11, 8)
    print(l)
    l.delete(1)
    l.delete(2)
    print(l)
main()