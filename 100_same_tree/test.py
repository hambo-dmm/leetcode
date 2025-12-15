import pytest

from solution import Solution
from TreeNode import TreeNode

instance = Solution()

def test_case_1():
    p = TreeNode.make_binary_tree([1,2,3])
    q = TreeNode.make_binary_tree([1,2,3])
     
    assert instance.isSameTree(p, q) == True

def test_case_2():
    p = TreeNode.make_binary_tree([1,2])
    q = TreeNode.make_binary_tree([1,None,2])
     
    assert instance.isSameTree(p, q) == False