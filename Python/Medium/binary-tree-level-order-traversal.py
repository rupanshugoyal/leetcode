# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        LOT = list()

        if root == None:
            return list()

        queue = list()
        queue.append(root)
        queue.append(None)

        parents = list()
        children = list()

        while len(queue) > 0:
            if queue[0] == None:
                queue += children
                if len(children) > 0:
                    queue.append(None)
                parents = [x.val for x in parents]
                LOT.append(parents)
                children = list()
                parents = list()
            else:
                if queue[0].left != None:
                    children.append(queue[0].left)
            
                if queue[0].right != None:
                    children.append(queue[0].right)

                parents.append(queue[0])
            queue.pop(0)
        return LOT
