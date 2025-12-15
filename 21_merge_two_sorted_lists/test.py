import pytest

from solution import Solution
from ListNode import ListNode
from ListNodeHelpers import ListNodeHelpers

instance = Solution()
list_node_helpers = ListNodeHelpers()

def test_case_1():
    list1 = list_node_helpers.createLinkedList([1,2,4])
    list2 = list_node_helpers.createLinkedList([1,3,4])
    expected = list_node_helpers.createLinkedList([1,1,2,3,4,4])

    assert list_node_helpers.compareTwoLinkedLists(instance.mergeTwoLists(list1, list2), expected) == True

def test_case_2():
    list1 = list_node_helpers.createLinkedList([])
    list2 = list_node_helpers.createLinkedList([])
    expected = list_node_helpers.createLinkedList([])

    assert list_node_helpers.compareTwoLinkedLists(instance.mergeTwoLists(list1, list2), expected) == True

def test_case_3():
    list1 = list_node_helpers.createLinkedList([])
    list2 = list_node_helpers.createLinkedList([0])
    expected = list_node_helpers.createLinkedList([0])

    assert list_node_helpers.compareTwoLinkedLists(instance.mergeTwoLists(list1, list2), expected) == True

def test_case_4():
    list1 = list_node_helpers.createLinkedList([])
    list2 = list_node_helpers.createLinkedList([0])
    expected = list_node_helpers.createLinkedList([0,1,2])

    assert list_node_helpers.compareTwoLinkedLists(instance.mergeTwoLists(list1, list2), expected) == False