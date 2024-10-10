class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # No se permiten duplicados

        self.update_height(root)

        balance = self.balance(root)

        # Casos de desequilibrio

        # Caso izquierda-izquierda
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Caso derecha-derecha
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Caso izquierda-derecha
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Caso derecha-izquierda
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.key)
            result += self.inorder_traversal(root.right)
        return result

    def print_tree(self):
        result = self.inorder_traversal(self.root)
        print(result)


# Ejemplo de uso
avl_tree = AVLTree()
keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for key in keys:
    avl_tree.insert_key(key)

avl_tree.print_tree()
