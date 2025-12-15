import pytest

from solution import Solution
from TreeNode import TreeNode

instance = Solution()

def test_case_1():
    root = TreeNode.make_binary_tree([1,2,2,3,4,4,3])
    
    assert instance.isSymmetric(root) == True

def test_case_2():
    root = TreeNode.make_binary_tree([1,2,2,None,3,None,3])
    
    assert instance.isSymmetric(root) == False

