import pytest

from TreeNode import TreeNode
from solution import Solution

instance = Solution()

def test_case_1():
    root = [3,9,20,None,None,15,7]
    binary_tree = TreeNode.make_binary_tree(root)

    assert instance.maxDepth(binary_tree) == 3

def test_case_2():
    root = [1,None,2]
    binary_tree = TreeNode.make_binary_tree(root)

    assert instance.maxDepth(binary_tree) == 2

def test_case_3():
    root = []
    binary_tree = TreeNode.make_binary_tree(root)

    assert instance.maxDepth(binary_tree) == 0