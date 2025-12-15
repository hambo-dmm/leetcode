# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from ListNode import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        dummy = ListNode()
        result = dummy
        
        while p and q:
            if p.val >= q.val:
                dummy.next = q
                q = q.next
            else:
                dummy.next = p
                p = p.next
            
            dummy = dummy.next

        if p:
            dummy.next = p
        elif q:
            dummy.next = q

        return result.next