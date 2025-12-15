from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __eq__(self, other) -> bool:
        if not isinstance(other, ListNode) and other is not None:
            return NotImplemented
        
        p = self
        q = other

        while p and q:
            if p.val != q.val:
                return False
            
            p, q = p.next, q.next
        
        return p is None and q is None

    def print(self):
        p = self
        while p:
            p = p.next
        

    @classmethod
    def create_linked_list(self, nums: List[int]):
        dummy = ListNode()
        root = dummy
        for num in nums:
            dummy.next = ListNode(num)
            dummy = dummy.next

        return root.next

    @staticmethod
    def set_link_by_indices(head, start_index: int = -1, end_index: Optional[int] = None) -> None:
        if not head:
            return

        # --- Pass 1: Get List Size and Start Node (if positive index) ---
        p = head
        list_size = 0
        
        # We need this node to be found during Pass 1, if possible
        start_node_at_index = None 

        while p:
            if start_index >= 0 and list_size == start_index:
                start_node_at_index = p
            
            p = p.next
            list_size += 1
            
        # Check if list is empty or index is out of bounds (positive)
        if list_size == 0 or (start_index >= 0 and start_index >= list_size):
            return

        # --- Resolve Start Node (Handles -1) ---
        start_node = None
        if start_index == -1:
            # Pass 2a: Find the Last Node (Tail)
            p = head
            while p.next:
                p = p.next
            start_node = p # p is now the tail
        else:
            start_node = start_node_at_index
            
        # Safety check: Should not happen if logic is correct, but good practice
        if not start_node:
            return

        # --- Resolve Target Node (Handles end_index) ---
        target_node = None
        
        # Check if end_index is provided and valid (0 <= end_index < list_size)
        if end_index is not None and 0 <= end_index < list_size:
            # Pass 2b: Find the Target Node by Index
            q = head
            current_index = 0
            while q:
                if current_index == end_index:
                    target_node = q
                    break
                q = q.next
                current_index += 1
        
        # --- Set the Link ---
        # If end_index is invalid or None, target_node remains None
        start_node.next = target_node