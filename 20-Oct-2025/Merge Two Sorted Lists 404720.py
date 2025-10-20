# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # check for edge cases
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        # make a new list and append the correct element to it
        start = ListNode()
        dummy = start
        while list1 and list2:
            print(list1.val, list2.val)
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        # append anything left in any of the lists
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        
        return start.next
        