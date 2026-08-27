# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = {}
        given = head 
        dummy = Node(0)
        ptr = dummy 

        while given:
            new_n = Node(given.val)
            hash[given] = new_n
            given = given.next
        
        given = head
        while given:
            new_n = hash[given]
            new_n_n = None
            new_n_r = None

            if given.next:
                new_n_n = hash[given.next]

            if given.random:
                new_n_r = hash[given.random]

            new_n.next = new_n_n
            new_n.random = new_n_r

            given = given.next
        
        if not head:
            return 
        dummy.next = hash[head]
        return dummy.next