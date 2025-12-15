from typing import Optional

from TreeNode import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._is_balanced_recursive(root) != -1

    def _is_balanced_recursive(self, node):
        if not node:
            return 0

        left = self._is_balanced_recursive(node.left)
        if left == -1:
            return -1

        right = self._is_balanced_recursive(node.right)
        if right == -1:
            return -1

        if abs(right - left) > 1:
            return -1

        return 1 + max(left, right)