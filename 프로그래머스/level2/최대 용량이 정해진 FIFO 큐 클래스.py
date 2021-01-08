class EmptyException:
    def __init__(self):
        return False


class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)


class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return len(self)

    def push(self, item):
        if len(self) < max_size:
            self.stack1.push(item)
            return True
        else:
            return False

    def pop(self):
        if len(self) == 0:
            raise EmptyException()
        else:
            return self.stack1.pop()


n, max_size = map(int, input().strip().split(' '))
print(n, max_size)