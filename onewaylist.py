class Element:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next   


class Onewaylist:
    def __init__(self):
        self.head = None
    
    def destroy(self):
        self.head = None

    def add(self, data):
        self.head = Element(data, self.head)

    def append(self, data):
        if self.head == None:
            self.head = Element(data)
        else:
            where = self.head
            while where.next != None:
                where = where.next
            where.next = Element(data)

    def remove(self):
        if self.head != None:
            self.head = self.head.next
        else:
            self.head = None

    def remove_end(self):
        if self.head != None:
            if self.head.next != None:
                where = self.head
                while where.next.next != None:
                    where = where.next
                where.next = None
            else:
                self.head = None
        else:
            self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

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
        return self.head.data

    def __str__(self):
        io = ''
        where = self.head
        while where != None:
            io += '-> ' + str(where.data) + '\n'
            where = where.next
        return io


def main():
    elements = [('AGH', 'Kraków', 1919),
                ('UJ', 'Kraków', 1364),
                ('PW', 'Warszawa', 1915),
                ('UW', 'Warszawa', 1915),
                ('UP', 'Poznań', 1919),
                ('PG', 'Gdańsk', 1945)]
    uczelnie = Onewaylist()
    uczelnie.append(elements[0])
    uczelnie.append(elements[1])
    uczelnie.append(elements[2])
    uczelnie.add(elements[3])
    uczelnie.add(elements[4])
    uczelnie.add(elements[5])
    print(uczelnie)
    print(uczelnie.length())
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.remove_end()
    uczelnie.append(elements[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())


main()