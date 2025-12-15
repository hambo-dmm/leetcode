from typing import Optional
from collections import deque

from TreeNode import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #return self._max_depth_recursive(root)
        return self._max_depth_iterative(root)

    def _max_depth_recursive(self, node):
        if not node:
            return 0

        left = self._max_depth_recursive(node.left) 
        right = self._max_depth_recursive(node.right) 

        return max(left, right) + 1

    def _max_depth_iterative(self, node):
        if not node:
            return 0

        result = 0
        queue = deque([node])

        while queue:
            result += 1
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return result