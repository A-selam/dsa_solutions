class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
            
    def add(self, key, val):
        new = self.Node(key, val)
        new.next = self.head.next
        new.prev = self.head
        self.head.next.prev = new
        self.head.next = new
        return new
    def remove(self, node):
       if node != self.head and node != self.tail:
            node.prev.next = node.next
            node.next.prev = node.prev
    def move_front(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def __init__(self, capacity: int):
        self.size = capacity
        self.dic = {}
        self.head = self.Node(-2, -1)
        self.tail = self.Node(-2, -1)
        self.head.next =self.tail
        self.tail.prev = self.head
        self.curr = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.move_front(node)
            return node.val
        else:
            return -1      

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.remove(node)
            self.move_front(node)
        elif len(self.dic) >= self.size:
            delete = self.tail.prev
            self.remove(delete)
            del self.dic[delete.key]
            node = self.add(key, value)
            self.dic[key] = node
        else:
            node = self.add(key, value)
            self.dic[key] = node
