class Element:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class Twowaylist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def destroy(self):
        where = self.head
        while where != None:
            where_next = where.next
            where.next = None
            where.prev = None
            where = where_next
        self.head = None
        self.tail = None

    def add(self, data):
        self.head = Element(data = data, next = self.head)
        if self.head.next != None:
            self.head.next.prev = self.head
        where = self.head
        while where.next != None:
            where = where.next
        self.tail = where

    def append(self, data):
        if self.head == None:
            self.head = Element(data)
            self.tail = self.head
        else:
            where = self.head
            while where.next != None:
                where = where.next
            where.next = Element(data = data, prev = where)
            self.tail = where.next

    def remove(self):
        if self.head != None:
            if self.head.next != None:
                self.head = self.head.next
                self.head.prev = None
        else:
            self.head = None

    def remove_end(self):
        if self.head != None:
            if self.head.next != None:
                where = self.head
                while where.next.next != None:
                    where = where.next
                where.next = None
                self.tail = where
            else:
                self.head = None
                self.tail = None
        else:
            self.head = None
            self.tail = None

    def is_empty(self):
        return self.head is None
    
    def length(self):
        if self.head != None:
            i = 0
            where = self.head
            while where != None:
                i += 1
                where = where.next
            return i
        else:
            return 0

    def get(self):
        return self.head.data if self.head is not None else None

    def __str__(self):
        io = ''
        where = self.head
        while where != None:
            io += '-> ' + str(where.data) + '\n'
            where = where.next
        return io
    
    def str_end(self):
        io = ''
        where = self.tail
        while where != None:
            io += '-> ' + str(where.data) + '\n'
            where = where.prev
        return io


def main():
    elements = [('AGH', 'Kraków', 1919),
                ('UJ', 'Kraków', 1364),
                ('PW', 'Warszawa', 1915),
                ('UW', 'Warszawa', 1915),
                ('UP', 'Poznań', 1919),
                ('PG', 'Gdańsk', 1945)]
    uczelnie = Twowaylist()
    uczelnie.append(elements[0])
    uczelnie.append(elements[1])
    uczelnie.append(elements[2])
    uczelnie.add(elements[3])
    uczelnie.add(elements[4])
    uczelnie.add(elements[5])
    print(uczelnie)
    print(uczelnie.str_end())
    print(uczelnie.length())
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print(uczelnie)
    print(uczelnie.str_end())
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.remove_end()
    uczelnie.append(elements[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())

main()