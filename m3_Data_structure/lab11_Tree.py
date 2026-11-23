class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, root, value):
            if value < root.value:
                if root.left is None:
                    root.left = TreeNode(value)
                else:
                    self.insert_recursive(root.left, value)
            else:
                if root.right is None:
                    root.right = TreeNode(value)
                else:
                    self.insert_recursive(root.right, value)


    def search(self, root, value):
        if root is None or root.value == value:
            return root
        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)


    def in_order_traversal(self, root, res=[]):
        if root:
            self.in_order_traversal(root.left, res)
            res.append(root.value)
            self.in_order_traversal(root.right, res)
        return res



def main():
    tree = BinTree()
    a = list(map(float, input("Введите элементы дерева: ").split(' ')))
    for value in a:
        tree.insert(value)
    sorted = tree.in_order_traversal(tree.root)
    print(sorted)

if __name__ == '__main__':
    main()