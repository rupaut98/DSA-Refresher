class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        current = self.head
        if current is None:
            self.head = Node(val)
        while current:
            current = current.next
        current.next = Node(val)

    def print_list(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.val)
            current = current.next
        return arr
    
    def search(self, val):
        current = self.head
        index = 0

        while current:
            if current.val == val:
                return index
            index += 1
            current = current.next
        return -1
    
    def delete_node(self,val):
        current = self.head
        prev = None

        if current and current.val == val:
            self.head = current.next
            return

        while current:
            if current.val == val:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def insert_after_node(self, val1, val2):
        current = self.head

        while current:
            if current.val == val1:
                new_node = Node(val1)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head

        while current:
            temp_node = current.next
            current.next = prev
            prev = current
            current = temp_node

        self.head = prev
            
