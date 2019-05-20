import sys


class ExtendedList(list):
    def __init__(self, l=[]):
        super().__init__(l)

    def __getattr__(self, name):
        if name == "reversed" or name == "R":
            return self[::-1]
        if name == "last" or name == "L":
            return self[-1]
        if name == "size" or name == "S":
            return len(self)
        if name == "first" or name == "F":
            return self[0]
        raise AttributeError

    def __setattr__(self, name, value):
        if name == "size" or name == "S":
            if value < len(self):
                while len(self) > value:
                    self.pop()
            else:
                while len(self) < value:
                    self.append(None)
            return self
        if name == "first" or name == "F":
            self[0] = value
            return self
        if name == "last" or name == "L":
            self[-1] = value
            return self
        raise AttributeError


exec(sys.stdin.read())
