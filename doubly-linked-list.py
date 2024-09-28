class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = Node(val)
        if not self.head and not self.tail:
            self.head = self.tail = new_node
            return

        if self.head and self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        
    def prepend(self, val):
        new_node = Node(val)
        if not self.head and not self.tail:
            self.head = self.tail = new_node
            return
        
        if self.head and self.tail:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        
    def delete_node(self, val):
        if not self.head and not self.tail:
            return

        if self.head.val == val:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = self.tail = None
            return
        
        if self.tail.val == val:
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = self.tail = None
            return
        
        current = self.head
        while current:
            if current.val == val:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                return
            current = current.next

    def print_list(self, reverse = False):

        current = self.tail if reverse else self.head
        list1 = []

        if not reverse and current:
            while current.next:
                list1.append(current.val)
                current = current.next
            print(list1)
        
        elif reverse and current:
            while current.prev:
                list1.append(current.val)
                current = current.prev
            print(list1)

        return
            

    def reverse_linked_list(self):
        previous = None
        current = self.head

        while current:
            temp_node = current.next
            current.next = previous
            current.prev = temp_node
            previous = current
            current = temp_node

        self.head = previous


        

        

        
