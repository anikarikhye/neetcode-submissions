# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Step-1: Start from root node and from there recursively go down each of the children node
Step-2: Store down the values starting from the root node to the current node in an array.
Step-3: If the value of current node is maximum in the array, return it
'''


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res 

        return dfs(root, root.val)  

        