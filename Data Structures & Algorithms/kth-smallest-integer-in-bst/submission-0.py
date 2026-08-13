# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Step-1: Convert the entire BST into an array by traversing recursively through each node and adding them in the order left-node-right 
Step-2: After all the nodes are in the array, find the k smallest element and return'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        
        def convert(node):
            if not node:
                return 
            convert(node.left)
            l.append(node.val)
            convert(node.right)
            
        convert(root)
        return l[k - 1]
        


        