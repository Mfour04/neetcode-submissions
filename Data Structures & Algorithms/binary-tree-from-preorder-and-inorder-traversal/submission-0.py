# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {value: i for i, value in enumerate(inorder)}
        preIndex = 0
        def dfs(left, right):
            nonlocal preIndex
            if left > right:
                return None
            
            rootValue = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootValue)
            mid = pos[rootValue]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        return dfs(0, len(inorder) - 1)
