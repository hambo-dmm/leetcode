from typing import List
from ListNode import ListNode

class ListNodeHelpers:

    def createLinkedList(self, nums: List[int]):
        dummy = ListNode()
        root = dummy
        for num in nums:
            dummy.next = ListNode(num)
            dummy = dummy.next

        return root.next

    def compareTwoLinkedLists(self, list1, list2):
        p, q = list1, list2

        while p and q:
            if p.val != q.val:
                return False
            p, q = p.next, q.next

        return p is None and q is None