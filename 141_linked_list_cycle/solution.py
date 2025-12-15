from typing import Optional

from ListNode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        p = head
        q = head


        while p and p.next:
            p = p.next.next
            q = q.next
            if p is q:
                return True

        return False