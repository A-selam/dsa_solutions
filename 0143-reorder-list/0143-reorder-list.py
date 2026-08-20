# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ptr = head 
        stack = []
        while ptr:
            stack.append(ptr)
            ptr = ptr.next
        
        n = len(stack)
        ptr = head
        lst = None
        for i in range(0, n//2):
            cur = stack.pop()
            temp = ptr.next
            ptr.next = cur
            cur.next = temp
            ptr = temp
        ptr.next = None
