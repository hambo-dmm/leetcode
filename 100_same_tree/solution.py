from typing import Optional
from TreeNode import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self._is_same_tree_recursive(p, q)
    
    def _is_same_tree_recursive(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False

        return self._is_same_tree_recursive(p.left, q.left) and self._is_same_tree_recursive(p.right, q.right)