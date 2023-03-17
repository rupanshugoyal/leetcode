# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# Solution

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return list()
        preorderTraverse = list()
        preorderTraverse.append(root.val)
        for child in root.children:
            preorderTraverse += self.preorder(child)
        return preorderTraverse