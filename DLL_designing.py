class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        
        if index < self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index - 1):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val):
        new_node = Node(val)
        if not self.head:  
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        if not self.tail: 
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        new_node = Node(val)
        prev_node = curr.prev
        
        prev_node.next = new_node
        new_node.prev = prev_node
        
        new_node.next = curr
        curr.prev = new_node
        
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0: 
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None  
        elif index == self.size - 1: 
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        self.size -= 1