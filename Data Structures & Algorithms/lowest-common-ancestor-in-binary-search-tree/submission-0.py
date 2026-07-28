# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Step-1: Start at the given root node of the tree
Step-2: From the root node, go to its children - left and right and keep repeating the process recursively till you reeach nodes p and q.
Step-3: Once you reach nodes p and q; store the paths taken to reach both nodes in a stack.
Step-4: In the two stacks from the bottom check the last common root and return it.
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        leftLCA=self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        
        if leftLCA and rightLCA:
            return root
        elif leftLCA is not None:
            return leftLCA
        else:
            return rightLCA

        
        