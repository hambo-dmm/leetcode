from typing import Optional
from TreeNode import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self._get_diameter_recursive(root)
        return self.result

    def _get_diameter_recursive(self, node):
        if not node:
            return 0

        left = self._get_diameter_recursive(node.left)
        right = self._get_diameter_recursive(node.right)

        self.result = max(self.result, left + right)

        return max(left, right) + 1