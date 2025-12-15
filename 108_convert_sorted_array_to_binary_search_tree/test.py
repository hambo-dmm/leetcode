import pytest

from solution import Solution
from TreeNode import TreeNode

instance = Solution()

def test_case_1():
    nums = [-10,-3,0,5,9]
    expected = TreeNode.make_height_balanced_binary_tree([-10,-3,0,5,9], 0, len(nums) - 1)
    
    result = instance.sortedArrayToBST(nums)
    expected.print()
    result.print()


    assert result.is_equivalent(expected) == True

def test_case_2():
    nums = [1,3]
    expected = TreeNode.make_height_balanced_binary_tree([1,3], 0, len(nums) - 1)
    
    result = instance.sortedArrayToBST(nums)

    assert result.is_equivalent(expected) == True