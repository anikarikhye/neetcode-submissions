# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Step-1: Calculate root of subtree and check if it is present in main tree.
Step-2: If not, return False; if found, go to the same root in the main tree.
Step-3: Once found, compare left and right children recursively of both nodes.
Step-4: If same, return True; else False
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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None
        if self.is_same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        