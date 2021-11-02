"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def remove_last_nth(node, k):
    last_k_plus_one_nodes = []
    list_size = 0
    first_node = node
    while node:
        list_size += 1
        if len(last_k_plus_one_nodes) > k:
            last_k_plus_one_nodes = last_k_plus_one_nodes[1:]
        last_k_plus_one_nodes.append(node)
        node = node.next

    if k == list_size:
        new_first_node = last_k_plus_one_nodes[1]
        first_node = new_first_node
    else:
        k_minus_one_node = last_k_plus_one_nodes[0]
        if k > 1:
            k_plus_one_node = last_k_plus_one_nodes[2]
            k_minus_one_node.next = k_plus_one_node
        else:
            k_minus_one_node.next = None
    return first_node


def get_list(n):
    lst = []
    while n:
        lst.append(n.val)
        n = n.next
    return lst


def node_from_list(lst):
    n = None
    for i in lst[::-1]:
        n = Node(val=i, next=n)
    return n


if __name__ == '__main__':

    lst = [1, 4, 5, 6, 7, 10, 9, 12, 45]
    k = 5
    list_first_node = node_from_list(lst)
    list_first_node = remove_last_nth(list_first_node, k)
    assert get_list(list_first_node) == lst[:len(lst) - k] + lst[-k + 1:]

    # Edge case, remove first element
    lst = [1, 4, 5, 6, 7, 10, 9, 12, 45, 23]
    k = 10
    list_first_node = node_from_list(lst)
    list_first_node = remove_last_nth(list_first_node, k)
    assert get_list(list_first_node) == lst[:len(lst) - k] + lst[-k + 1:]

    # Edge case, remove last element
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 1
    list_first_node = node_from_list(lst)
    list_first_node = remove_last_nth(list_first_node, k)
    assert get_list(list_first_node) == lst[:len(lst) - k]
