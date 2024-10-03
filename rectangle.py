class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        return iter([{'length': self.length}, {'width': self.width}])

rectangle = Rectangle(5, 3)

for i in rectangle:
    print(i)
