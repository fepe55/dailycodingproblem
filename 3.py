import json

"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string back
into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def _serialize_helper(cls, node):
        node_list = []

        left = None
        right = None
        if node.left:
            left = cls._serialize_helper(node.left)
        if node.right:
            right = cls._serialize_helper(node.right)
        node_list = [node.val, left, right]
        return node_list

    @classmethod
    def _deserialize_helper(cls, node_list):
        val = node_list[0]
        left = node_list[1]
        right = node_list[2]
        left_node = None
        right_node = None
        if left:
            left_node = cls._deserialize_helper(left)
        if right:
            right_node = cls._deserialize_helper(right)
        return Node(val, left_node, right_node)

    def serialize(self):
        node_list = [self._serialize_helper(self)]
        return json.dumps(node_list)

    @classmethod
    def deserialize(cls, string):
        node_list = json.loads(string)
        root = node_list[0]
        node = cls._deserialize_helper(root)
        return node

    def __str__(self):
        return self.serialize()


if __name__ == '__main__':
    node = Node(
        'root',
        Node(
            'left',
            Node('left.left')
        ),
        Node('right')
    )
    print(node)
    serialized_node = node.serialize()
    print(serialized_node)
    deserialized_node = Node.deserialize(serialized_node)
    print(deserialized_node)
    # assert deserialize(serialize(node)).left.left.val == 'left.left'
    print(Node.deserialize(node.serialize()).left.left.val == 'left.left')
