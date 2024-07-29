class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    
    def insert(self, val):
        node = self.head
        new_node = Node(val)
        
        if node is None:
            self.head = new_node
            return
        
        if node.next is None:
            node.next = new_node
            return
        
        while node.next is not None:
            node = node.next
        
        node.next = new_node


    def insert_at_index(self, index, val):
        node = self.head
        new_node = Node(val)
        
        i = 0
        
        if i == index:
            new_node.next = node
            self.head = new_node
            return
        
        if node.next is None:
            if index == 1:
                self.head.next = new_node
                return
            else:
                return None
        
        while node is not None:
            i += 1
            
            if i == index:
                if node.next is not None:
                    new_node.next = node.next
                    node.next = new_node
                    return
                else:
                    node.next = new_node
                    return
            
            node = node.next
        
        return None

    
    def remove(self, val):
        node = self.head
        
        if node.val == val:
            self.head = node.next
            return
        
        while node:
            if node.next is not None:
                if node.next.val == val:
                    node.next = node.next.next
                    return
            node = node.next


    def get_values(self):
        data = []
        node = self.head
        
        while node is not None:
            data.append(node.val)
            node = node.next
        
        return data


    def get_index(self, val):
        node = self.head
        
        if node.val == val:
            return 0
        
        i = 0
        
        while node.next:
            i += 1
            node = node.next
            
            if node.val == val:
                return i
        
        return None


    def get_size(self):
        i = 0
        node = self.head
        
        while node:
            i += 1
            node = node.next
        
        return i


    def includes(self, val):
        node = self.head
        
        while node:
            if node.val == val:
                return True
            node = node.next
        
        return False
