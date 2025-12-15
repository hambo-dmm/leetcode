from typing import Optional
from collections import deque

from TreeNode import TreeNode

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._is_symmetric_recursive(root, root)

    def _is_symmetric_recursive(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self._is_symmetric_recursive(p.left, q.right) and self._is_symmetric_recursive(p.right, q.left)