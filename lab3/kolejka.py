
class Kolejka:
    def __init__(self, size = 5):
        self.tab = [None for i in range(size)]
        self.size = size
        self.save = 0
        self.read = 0

    def is_empty(self):
        return self.save == self.read
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.read]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            element = self.tab[self.read]
            self.tab[self.read] = None
            self.read = self.read + 1
            if self.read == self.size and self.read != self.save:
                self.read = 0
            return element

    def enqueue(self, data):
        self.tab[self.save] = data
        self.save = self.save + 1
        if self.save == self.size:
            self.save = 0
        if self.save == self.read:
            newtab = [None for i in range(2*self.size)]
            for i in range(self.save, self.size):
                newtab[self.size + i] = self.tab[i]
            for i in range(self.save):
                newtab[i] = self.tab[i]
            self.tab = newtab
            self.read = self.read + self.size
            self.size = self.size*2
    


    def __str__(self):
        io = '['
        if self.read <= self.save:
            for i in range(self.read, self.save):
                io += str(self.tab[i])
                if i != self.save - 1:
                    io += ', '
        else:
            for i in range(self.read, self.size):
                io += str(self.tab[i]) 
                if self.save == 0 and i == self.size - 1:
                    break
                io += ', '
            for i in range (self.save):
                io += str(self.tab[i])
                if i != self.save - 1:
                    io += ', '
        io += ']'
        return io
    
    def state(self):
        print(self.tab)

def main():
    k = Kolejka()
    k.enqueue(1)
    k.enqueue(2)
    k.enqueue(3)
    k.enqueue(4)
    print(k.dequeue())
    print(k.peek())
    print(k)
    k.enqueue(5)
    k.enqueue(6)
    k.enqueue(7)
    k.enqueue(8)
    k.state()
    while not k.is_empty():
        print(k.dequeue())    
    print(k)

main()
