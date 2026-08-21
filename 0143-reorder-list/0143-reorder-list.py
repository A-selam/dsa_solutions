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
        # break into half
        slow = head
        quick = head.next
        while quick:
            if not quick.next:
                break 
            slow = slow.next
            quick = quick.next.next

        # reverse the later half 
        mid = slow.next
        slow.next = None

        ptr1 = None
        ptr2 = mid
        while ptr2:
            ptr3 = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = ptr3
        
        # merge
        m_ptr1 = head
        m_ptr2 = ptr1
        while m_ptr1 and m_ptr2:
            t_ptr1 = m_ptr1.next
            t_ptr2 = m_ptr2.next
            
            m_ptr1.next = m_ptr2
            m_ptr2.next = t_ptr1

            m_ptr1 = t_ptr1
            m_ptr2 = t_ptr2
