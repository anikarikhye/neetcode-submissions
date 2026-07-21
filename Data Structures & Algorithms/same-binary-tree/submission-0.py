# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""Steps
Step-1: Find the root nodes for both trees p and q.
Step-2: Traverse down the root node by calling left and right children recursively. 
Step-3: Compare values of nodes at each step and if not matching, return False.
Step-4: Return True if values are same even after reaching all the leaf nodes.
"""

class Solution:
    def is_same(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        left_same = self.is_same(node1.left, node2.left)
        right_same = self.is_same(node1.right, node2.right)
        return left_same and right_same

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.is_same(p, q)
            
        
        