class Stack:
    def __init__(self) -> None:
        self.itmes = []

    def is_empty(self):
        # return len(self.itmes) == 0
        return not self.itmes

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.pop(item)

    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.itmes)


if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
