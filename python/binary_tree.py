class Node:
    def __init__(self, data : int):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'data: {self.data}'

    def insert(self, data : int):
        if self.data > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def pre_order(self):
        print(self)
        if self.left is not None:
            self.left.pre_order()
        if self.right is not None:
            self.right.pre_order()

    def in_order(self):
        if self.left is not None:
            self.left.in_order()
        print(self)
        if self.right is not None:
            self.right.in_order()

    def post_order(self):
        if self.left is not None:
            self.left.post_order()
        if self.right is not None:
            self.right.post_order()
        print(self)


if __name__ == '__main__':
    arr = [4, 34, 14, 13, 15, 45, 44, 48, 47, 49]
    root = Node(40)

    for v in arr:
        root.insert(v)

    # root.pre_order()
    # root.in_order()
    root.post_order()