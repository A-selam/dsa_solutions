class Node:
    def __init__(self, val, key):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.cap = capacity

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        node = self.remove(key)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(key)

        node = Node(value, key)
        self.dict[key] = node
        self.insert(node)

        if len(self.dict) > self.cap:
            lru = self.tail.prev
            self.remove(lru.key)
            del self.dict[lru.key]

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def remove(self, key):
        node = self.dict[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)