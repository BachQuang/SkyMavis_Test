class Node():
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
class DoubleLinkList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def push_front(self, value):
        if self.size == 0:
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1
    def push_back(self, value):
        if self.size == 0:
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = self.tail.next
        self.size += 1
    def pop_front(self):
        value = None
        if self.size == 1:
            value = self.head.val
            self.head = None
            self.tail = None
            self.size -= 1     
        elif self.size > 1:
            value = self.head.val
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        return value
    def pop_back(self):
        value = None
        if self.size == 1:
            value = self.tail.val
            self.head = None
            self.tail = None
            self.size -= 1
        elif self.size > 1:
            value = self.tail.val
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        return value
    def getArray(self):
        res = []
        root = self.head
        while root:
            res.append(root.val)
            root = root.next
        return res

if __name__ == "__main__":
    x = DoubleLinkList()
    x.push_back(21)
    # print(x.pop_back())
    print(x.getArray())
    print(x.pop_front())
    print(x.getArray())
    x.push_back(443)
    x.push_back(21120)
    print(x.getArray())
    print(x.pop_front())
    print(x.getArray())