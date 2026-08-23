class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def insert(self, value):
        temp = self.head
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            while temp is not None and temp.next is not None:
                temp = temp.next
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        return True

    def pop(self):
        temp = self.head
        prev = self.head
        while temp is not None and temp.next is not None:
            prev = temp
            temp = temp.next
        if self.head is None:
            return self.head
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def get(self, idx):
        if idx <0 or idx >= self.length:
            return None
        temp = self.head
        for _ in range(idx):
            temp = temp.next
        return temp


my_linked_list = LinkedList(4)
my_linked_list.insert(6)
my_linked_list.insert(7)

