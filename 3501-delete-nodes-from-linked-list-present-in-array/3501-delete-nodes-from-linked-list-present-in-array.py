# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ans.next = head
        prev = ans
        curr = ans.next
        
        nums = set(nums)
        while curr:
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return ans.next