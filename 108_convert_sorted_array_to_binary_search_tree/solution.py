from typing import Optional
from typing import List

from TreeNode import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self._sorted_array_to_bst_recursive(nums, 0, len(nums) - 1)

    def _sorted_array_to_bst_recursive(self, nums, left, right):
        if left > right:
            return None

        middle = (left + right) // 2

        node = TreeNode(nums[middle])
        
        node.left = self._sorted_array_to_bst_recursive(nums, left, middle - 1)
        node.right = self._sorted_array_to_bst_recursive(nums, middle + 1, right)

        return node