class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class sll:
    def __init__(self):
        self.head = None
        self.tail = None
    def create(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            newnode = Node(data)
            self.tail.next = newnode
            self.tail = newnode
    def arr(self):
        temp = self.head
        i = 1
        odd = []
        even = []
        while temp is not None:
            if i % 2 == 1:
                odd.append((temp.data, id(temp.next)))
            else:
                even.append((temp.data, id(temp.next))) 
            i += 1
            temp = temp.next
        a = odd + even
        print(a)
obj = sll()
n = int(input())
for i in range(n):
    m = int(input())
    obj.create(m)
obj.arr()
