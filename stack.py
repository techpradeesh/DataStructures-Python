class Stack:
    def __init__(self): # constructor
        self.items = []

    def is_empty(self): 
        return not self.items

    def push_item(self, item):
        return self.items.append(item)

    def pop_item(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self): #Makes the self.items printable by converting it to an string
        return str(self.items)


if __name__ == "main":
    s = Stack()

    s.push_item(5)
    s.push_item(6)
    s.push_item(7)
    s.push_item(8)
    print(s.size())
    s.pop_item()

    print(s.size())
    print(s)
    print(s.is_empty())

