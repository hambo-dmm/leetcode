import pytest

from solution import Solution
from TreeNode import TreeNode

instance = Solution()

def test_case_1():
    root = TreeNode.make_binary_tree([3,4,5,1,2])
    sub_root = TreeNode.make_binary_tree([4,1,2])

    assert instance.isSubtree(root, sub_root) == True


def test_case_2():
    root = TreeNode.make_binary_tree([3,4,5,1,2,None,None,None,None,0])
    sub_root = TreeNode.make_binary_tree([4,1,2])

    assert instance.isSubtree(root, sub_root) == False

def test_case_3():
    root = TreeNode.make_binary_tree([3,4,5,1,None,2])
    sub_root = TreeNode.make_binary_tree([3,1,2])

    assert instance.isSubtree(root, sub_root) == False