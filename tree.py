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
        stack = [node]  #[10]

        while stack:
            current = stack.pop() #current = 10 # current = 5

            print(current.val)

            if current.right: #stack = [15] #stack = [15, 7]
                stack.append(current.right)

            if current.left:
                stack.append(current.left) #stack = [15, 5] #stack = [15,7,3]

    def post_order_traversal_iterative(self, node):
        if node is None:
            return
        
        stack1 = [node]
        stack2 = []

        while stack1:
            current = stack1.pop()

            stack2.append(current)

            if current.left:
                stack1.append(current.left)

            if current.right:
                stack1.append(current.right)

        while stack2:
            current = stack2.pop()
            print(current.val)
    

    #     10
    #    /  \
    #   5    15
    #  / \     \
    # 3   7     20
    def find_height_recursive(self, node):
        if node is None:
            return -1
        
        left_subtree = self.find_height_recursive(node.left)
        right_subtree = self.find_height_recursive(node.right)

        return max(left_subtree, right_subtree) + 1
    
    def find_height_iterative(self, node):
        if not node:
            return -1
        
        stack = [(self.root, 0)]
        max_height = 0 

        while stack:

            current_node, current_height = stack.pop()

            max_height = max(max_height, current_height)

            if  current_node.left:
                stack.append(current_node.left, current_height + 1)

            if current_node.right:
                stack.append(current_node.right, current_height + 1)

        return max_height
    
     #     10
    #    /  \
    #   5    15
    #  / \     \
    # 3   7     20
    def find_height_iterative(self, node):
        if not node:
            return -1

        stack = [(self.root, 0)]
        max_height = 0

        while stack:
            current_node, current_height = stack.pop()

            max_height = max(current_height, max_height)

            if current_node.left:
                stack.append(current_node.left, current_height.height)

            if current_node.right:
                stack.append(current_node.right, current_height + 1)

        return max_height


    def find_depth(self, node, val):
        if not node:
            return -1
        
        stack = [(node,0)]

        while stack:
            current_node, current_depth = stack.pop()

            if current_node.val == val:
                return current_depth
            
            if current_node.val < val and current_node.right:
                stack.append((current_node.right, current_depth + 1))

            elif current_node.val > val and current_node.left:
                stack.append((current_node.left, current_depth + 1))    

    def find_depth_recursive(self, node, depth, val):
        if not node:
            return -1

        if node.val == val:
            return depth
        
        if node.val < val:
            return self.find_depth_recursive(node.right, depth + 1, val) if node.right else - 1
        
        elif node.val > val:
            return self.find_depth_recursive(node.left, depth + 1, val) if node.left else -1
        
    def find_diameter(self):
        max_diameter = 0

        def calculate_height(node):
            if node is None:
                return 0 
            
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)

            current_diameter = left_height + right_height

            max_diameter = max(max_diameter, current_diameter)

            return max(left_height, right_height) + 1
        
        calculate_height(self.root)

        return max_diameter

        
        


        

        

        
            
        