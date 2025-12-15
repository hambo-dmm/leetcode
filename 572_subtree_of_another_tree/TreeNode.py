from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_equivalent(self, other_tree: Optional['TreeNode']) -> bool:
        return self._check_equivalence(self, other_tree)

    def print(self):
            if not self:
                return

            queue = deque()
            queue.append(self)

            while queue:
                level_size = len(queue)
                current_level_values = []
                
                # Flag to check if we saw any real node in this level
                found_actual_node = False
                
                for _ in range(level_size):
                    curr = queue.popleft()
                    
                    if curr is None:
                        current_level_values.append('null')
                        # Do NOT enqueue children for a None node
                    else:
                        current_level_values.append(curr.val)
                        found_actual_node = True # Found a real node
                        
                        # Enqueue children, including None, to maintain structure spacing
                        queue.append(curr.left)
                        queue.append(curr.right)
                
                # If we didn't find any actual node in the entire level, we can stop.
                # This prevents infinite printing of 'null null null...'
                if not found_actual_node:
                    break 

                # Print the current level's values
                print(" ".join(map(str, current_level_values)))

    def _check_equivalence(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return self._check_equivalence(p.left, q.left) and self._check_equivalence(p.right, q.right)


    # 2. The factory method for creating a tree from a list
    @classmethod
    def make_binary_tree(cls, nums: List[Optional[int]]) -> Optional['TreeNode']:
        if not nums or nums[0] is None:
            return None

        # cls refers to the TreeNode class
        root = cls(nums[0])
        queue = deque()
        
        # Using a tuple instead of TreeNodeAndIndex is often simpler in Python
        # Tuple format: (node, index)
        queue.append((root, 0))

        while queue:
            curr_node, curr_index = queue.popleft()
            
            # generate indices for children
            left_index = 2 * curr_index + 1
            right_index = left_index + 1
            
            # --- Logic to handle None values in the input list ---
            
            # 1. Handle Left Child
            left = None
            if left_index < len(nums) and nums[left_index] is not None:
                left = cls(nums[left_index])
                
            # 2. Handle Right Child
            right = None
            if right_index < len(nums) and nums[right_index] is not None:
                right = cls(nums[right_index])
            
            # assign to current parent node
            curr_node.left = left
            curr_node.right = right
            
            # add to the queue if they're not none
            if left is not None:
                queue.append((left, left_index))
            if right is not None:
                queue.append((right, right_index))

        return root

    @classmethod
    def make_height_balanced_binary_tree(cls, nums: List[Optional[int]], left: int, right: int) -> Optional['TreeNode']:
        if left > right:
            return None

        middle = (left + right) // 2

        node = TreeNode(nums[middle])
        
        node.left = TreeNode.make_height_balanced_binary_tree(nums, left, middle - 1)
        node.right = TreeNode.make_height_balanced_binary_tree(nums, middle + 1, right)

        return node