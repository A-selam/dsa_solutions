# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        l = 0
        while ptr:
            ptr = ptr.next
            l += 1
        
        if l == 1:
            return 

        target = l-n-1
        ptr = head 
        temp = 0
        # print(l, n, target)
        if target == -1:
            return head.next
        while temp < target:
            ptr = ptr.next
            temp += 1
        # print(ptr)
        if ptr.next:
            ptr.next = ptr.next.next
        

        return head 