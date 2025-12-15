from typing import Optional
from collections import deque

from TreeNode import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self._is_sub_tree_recursively(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def _is_sub_tree_recursively(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        left = self._is_sub_tree_recursively(p.left, q.left)
        right = self._is_sub_tree_recursively(p.right, q.right)

        return left and right