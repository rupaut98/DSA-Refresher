class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Tree(val)
        if not self.root:
            self.root = new_node
            return

        current = self.root

        while True:
            if current.val < val:
                if not current.right:
                    current.right = new_node
                    break
                current = current.right
            else:
                if not current.left:
                    current.left = new_node
                    break
                current = current.left

    def in_order_traversal_recursive(self, node):
        if not node:
            return None
        
        self.in_order_traversal_recursive(node.left)
        print(node.val, end = " ")
        self.in_order_traversal_recursive(node.right)
    
    #     10
    #    /  \
    #   5    15
    #  / \     \
    # 3   7     20

    def pre_order_traversal_recursive(self, node):
        if not node:
            return None
        
        print(node.val, end = " ")
        self.in_order_traversal_recursive(node.left)
        self.in_order_traversal_recursive(node.right)

    def post_order_traversal_recursive(self, node):
        if not node:
            return None
        
        self.in_order_traversal_recursive(node.left)
        self.in_order_traversal_recursive(node.right)
        print(node.val, end = " ")

    def in_order_traversal_iterative(self, node):
        stack = []
        current = node

        while current or stack:
            while current:
                stack.append(current.val)
                current = current.left
        
            current = stack.pop()
            print(current.val, end = " ")

            current = current.right

        
        # [10, 5, 3]
        # 3
        # [10]
        # 5
        # [10, 7]

        # [10]
        # []
        # [15]
        # []
        # [20]


    #     10
    #    /  \
    #   5    15
    #  / \     \
    # 3   7     20

    def pre_order_traversal_iterative(self, node):
        stack = [node]

        while stack:
            current = stack.pop()

            print(current.val)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)


        

        
            
        